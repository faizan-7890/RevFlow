import asyncio
import json
import os
from pathlib import Path
import edge_tts

ROOT = Path(r"C:\Users\Faizan J\Desktop\AIvoicebuilder")
TRANSCRIPTS_DIR = ROOT / "recordings" / "transcripts"
RECORDINGS_DIR = ROOT / "recordings"
PUBLIC_AUDIO_DIR = ROOT / "public" / "assets" / "audio"

async def generate_turn_audio(text: str, voice: str, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    communicator = edge_tts.Communicate(text, voice)
    await communicator.save(str(out_path))

async def process_scenario(json_path: Path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    scenario_id = data["id"]
    turns = data.get("turns", [])
    print(f"\n[+] Processing Scenario: {scenario_id} ({len(turns)} turns)...")
    
    turn_files = []
    turns_dir = RECORDINGS_DIR / "turns" / scenario_id
    turns_dir.mkdir(parents=True, exist_ok=True)
    
    for idx, turn in enumerate(turns):
        role = turn.get("role", "speaker")
        voice = turn.get("voice", "en-IN-NeerjaNeural")
        text = turn.get("text", "")
        
        turn_filename = f"{idx+1:02d}_{role}.mp3"
        turn_path = turns_dir / turn_filename
        
        print(f"  - Turn {idx+1}/{len(turns)} ({role} | {voice}): \"{text[:45]}...\"")
        await generate_turn_audio(text, voice, turn_path)
        turn_files.append(turn_path)
        await asyncio.sleep(0.3)
    
    master_mp3_path = RECORDINGS_DIR / f"{scenario_id}.mp3"
    public_mp3_path = PUBLIC_AUDIO_DIR / f"{scenario_id}.mp3"
    public_mp3_path.parent.mkdir(parents=True, exist_ok=True)
    
    combined_bytes = bytearray()
    for t_file in turn_files:
        with open(t_file, "rb") as tf:
            combined_bytes.extend(tf.read())
            
    with open(master_mp3_path, "wb") as mf:
        mf.write(combined_bytes)
        
    with open(public_mp3_path, "wb") as pf:
        pf.write(combined_bytes)
        
    print(f"  [OK] Saved Master Audio: {master_mp3_path} ({len(combined_bytes)} bytes)")
    print(f"  [OK] Copied to Public Web App: {public_mp3_path}")

async def main():
    json_files = sorted(TRANSCRIPTS_DIR.glob("*.json"))
    if not json_files:
        print("No transcript json files found!")
        return
        
    print(f"Found {len(json_files)} scenario transcripts to synthesize.")
    for jf in json_files:
        await process_scenario(jf)
        
    print("\n[SUCCESS] All 5 scenario audio files synthesized and exported successfully!")

if __name__ == "__main__":
    asyncio.run(main())
