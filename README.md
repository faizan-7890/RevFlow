# Divyasree "Whispers of the Wind" — Outbound AI Voice Agent

An outbound AI Voice Consultant named **Meera** engineered for **Divyasree Developers** to qualify prospective high-net-worth buyers for **Whispers of the Wind (WOW)**, a private-valley villa-plot community in Nandi Valley, near Nandi Hills, North Bengaluru.

---

## 🌟 Deliverables Summary

| Deliverable | Description & File Link |
|---|---|
| **System Prompt PDF** | [**`Divyasree-WOW-Voice-Agent-System-Prompt.pdf`**](file:///C:/Users/Faizan%20J/Desktop/AIvoicebuilder/docs/Divyasree-WOW-Voice-Agent-System-Prompt.pdf) — Formatted System Message, Phonetic Dictionary, Guardrails & Tools. |
| **Product Requirements Document (PRD)** | [**`WOW-voice-agent-PRD.pdf`**](file:///C:/Users/Faizan%20J/Desktop/AIvoicebuilder/docs/WOW-voice-agent-PRD.pdf) — Complete product requirements, user stories, metrics & test matrix. |
| **Audio Recordings (5 Flows)** | High-fidelity neural audio for 5 conversational test scenarios in [`recordings/`](file:///C:/Users/Faizan%20J/Desktop/AIvoicebuilder/recordings). |
| **Interactive Showcase & Simulator** | Web Application with audio scrubber, synchronized transcript, state tracker, and live simulator in [`public/`](file:///C:/Users/Faizan%20J/Desktop/AIvoicebuilder/public). |

---

## 🎧 The 5 Test Conversation Audio Flows

All 5 conversations are synthesized with neural Indian English and Hindi voices (`en-IN-NeerjaNeural`, `en-IN-PrabhatNeural`, `hi-IN-SwaraNeural`, `hi-IN-MadhurNeural`) with realistic pacing:

1. **Flow 1: Qualified Weekend Home Buyer (Self-Use)**
   - **Audio:** [`01-qualified-self-use.mp3`](file:///C:/Users/Faizan%20J/Desktop/AIvoicebuilder/recordings/01-qualified-self-use.mp3)
   - **Transcript:** [`01-qualified-self-use.json`](file:///C:/Users/Faizan%20J/Desktop/AIvoicebuilder/recordings/transcripts/01-qualified-self-use.json)
   - **Outcome:** Passes all 4 checkpoints (Intent: Self-use, Geo: Nandi Valley, Budget: ₹1–1.5 Cr, Timeline: Dec 2029 comfortable). Delivers Private Valley pitch and books expert callback.

2. **Flow 2: Dubai NRI Investor (Upfront Info & ROI Handling)**
   - **Audio:** [`02-nri-investment.mp3`](file:///C:/Users/Faizan%20J/Desktop/AIvoicebuilder/recordings/02-nri-investment.mp3)
   - **Transcript:** [`02-nri-investment.json`](file:///C:/Users/Faizan%20J/Desktop/AIvoicebuilder/recordings/transcripts/02-nri-investment.json)
   - **Outcome:** Prospect volunteers intent, geography, and ₹2 Cr budget in turn 1. Meera **does not re-ask** those points, explains 74% open density, deflects ROI guarantee professionally, and books weekend video consultation.

3. **Flow 3: Budget Fit but Location Mismatch (Whitefield Commuter)**
   - **Audio:** [`03-budget-fit-location-mismatch.mp3`](file:///C:/Users/Faizan%20J/Desktop/AIvoicebuilder/recordings/03-budget-fit-location-mismatch.mp3)
   - **Transcript:** [`03-budget-fit-location-mismatch.json`](file:///C:/Users/Faizan%20J/Desktop/AIvoicebuilder/recordings/transcripts/03-budget-fit-location-mismatch.json)
   - **Outcome:** Strong budget (₹2 Cr) but requires daily weekday commute to Whitefield. Meera validates the commute reality without arguing and gracefully ends call.

4. **Flow 4: Irritated Lead / DND Request**
   - **Audio:** [`04-irritated-user.mp3`](file:///C:/Users/Faizan%20J/Desktop/AIvoicebuilder/recordings/04-irritated-user.mp3)
   - **Transcript:** [`04-irritated-user.json`](file:///C:/Users/Faizan%20J/Desktop/AIvoicebuilder/recordings/transcripts/04-irritated-user.json)
   - **Outcome:** Lead is in a meeting and demands removal. Meera immediately de-escalates, logs `do_not_contact`, apologizes, and ends call.

5. **Flow 5: Hindi / Hinglish Bilingual Lead**
   - **Audio:** [`05-hindi-english.mp3`](file:///C:/Users/Faizan%20J/Desktop/AIvoicebuilder/recordings/05-hindi-english.mp3)
   - **Transcript:** [`05-hindi-english.json`](file:///C:/Users/Faizan%20J/Desktop/AIvoicebuilder/recordings/transcripts/05-hindi-english.json)
   - **Outcome:** Smooth code-switching to polite, natural Hindi/Hinglish, qualifies second home + investment intent, and schedules joint briefing for buyer and spouse.

---

## 🏛️ Conversation Architecture & The 4 Fitment Checkpoints

```
[ OUTBOUND CALL INITIATED ]
            │
            ▼
┌────────────────────────────────────────────────────────┐
│ 1. PERMISSION GATE (Mandatory)                        │
│ Introduce Meera + Divyasree + Whispers of the Wind     │
│ "Do you have a couple of minutes to speak?"            │
└────────────────────────────────────────────────────────┘
     │                                    │
 [Declined / Busy]                    [Agreed]
     ▼                                    ▼
Graceful exit / Callback      ┌──────────────────────────────────────────────┐
                              │ 2. THE 4 QUALIFICATION CHECKPOINTS           │
                              │ 1. Intent: Self-use vs. Investment           │
                              │ 2. Geography: Nandi Hills corridor comfort   │
                              │ 3. Budget: ₹92.4 Lakh+ starting price fit    │
                              │ 4. Timeline: Phased delivery (Dec 2029)      │
                              │ *No re-asking of volunteered info*           │
                              └──────────────────────────────────────────────┘
                                                   │
                              ┌────────────────────┴───────────────────┐
                              ▼                                        ▼
                   [Mismatch / Disqualified]                      [Qualified]
                              │                                        │
                 Log outcome via tool:                                 ▼
              • location_mismatch                     ┌────────────────────────────────┐
              • budget_mismatch                       │ 3. THE VALLEY PITCH (20–35s)   │
              • do_not_contact                        │ 74% open space, 20k sq.ft club,│
                              │                       │ eco-parks & scenic hill views  │
                              ▼                       └────────────────────────────────┘
                          End call                                     │
                                                                       ▼
                                                      ┌────────────────────────────────┐
                                                      │ 4. CTA & EXPERT HANDOFF        │
                                                      │ Book follow-up with Property   │
                                                      │ Expert (time, name, notes)     │
                                                      └────────────────────────────────┘
                                                                       │
                                                                       ▼
                                                      Trigger schedule_expert_callback
                                                                       │
                                                                       ▼
                                                            Silent end_call
```

---

## 🗣️ Phonetic Pronunciation Guide

| Written Entity | Spoken Phonetic Guide | IPA | Context & Telephony Rules |
|---|---|---|---|
| **Divyasree** | `Div-yaa-shree` | `/d̪ɪvˈjaːʃriː/` | Soft dental 'D', stress on 'shree' |
| **Nandi / Nandi Hills** | `Nun-dhee` / `Nun-dhee Hills` | `/ˈnʊn̪d̪ʱi/` | Soft aspirated 'dh', avoids harsh English 'nan-dee' |
| **Devanahalli** | `Dev-uh-nuh-HUL-lee` | `/d̪eːʋənəˈhʌlli/` | Airport corridor landmark |
| **Bengaluru** | `Ben-guh-LOO-roo` | `/beŋɡəˈluːɾu/` | Standard localized name |
| **₹92.4 lakh** | `ninety-two point four lakh` | `/ləkʰ/` | Spoken natural words; never raw symbols |
| **₹2.46 crore** | `two point four six crore` | `/kɾoːɾ/` | Say 'kror' smoothly |
| **December 2029** | `December twenty twenty-nine` | — | Spoken natural decade cadence |
| **1,200 – 3,199 sq.ft.** | `twelve hundred to about thirty-two hundred sq feet`| — | Natural unit phrasing |

---

## 📂 Project Directory Structure

```
AIvoicebuilder/
├── docs/
│   ├── Divyasree-WOW-Voice-Agent-System-Prompt.pdf    # Full System Message & Phonetics PDF
│   └── WOW-voice-agent-PRD.pdf                         # Product Requirements Document PDF
├── prompts/
│   ├── system-prompt.md                                # 322-line production system message
│   ├── project-knowledge.md                            # Canonical facts & negative guardrails
│   ├── pronunciation.json                              # Phonetic substitutions & IPA guide
│   ├── tools.json                                      # Function calling schemas
│   └── greeting.txt                                    # Telephony opening hook
├── public/
│   ├── index.html                                      # Interactive web showcase & simulator
│   ├── css/styles.css                                  # Custom luxury design system
│   ├── js/app.js                                       # Interactive player & bot simulator
│   └── assets/
│       ├── audio/ (01 to 05 master mp3 recordings)
│       └── docs/ (PDF downloads)
├── recordings/
│   ├── 01-qualified-self-use.mp3
│   ├── 02-nri-investment.mp3
│   ├── 03-budget-fit-location-mismatch.mp3
│   ├── 04-irritated-user.mp3
│   ├── 05-hindi-english.mp3
│   └── transcripts/ (01 to 05 JSON scenario dialogue scripts)
├── scripts/
│   ├── generate_audio.py                               # Edge-TTS synthesizer script
│   ├── generate_system_prompt_pdf.py                   # System prompt PDF generator
│   └── generate_prd_pdf.py                             # PRD PDF generator
├── server/
│   ├── server.py                                       # Python HTTP server
│   └── server.js                                       # Node.js HTTP server
├── package.json
└── README.md
```

---

## 🚀 How to Run Locally

### Option 1: Using Python
```bash
python server/server.py
```
Open [**`http://localhost:8080`**](http://localhost:8080) in your browser.

### Option 2: Using Node.js
```bash
npm start
```
Open [**`http://localhost:8080`**](http://localhost:8080) in your browser.

### Regenerating Assets (Optional)
- **Audio Files:** `python scripts/generate_audio.py`
- **System Prompt PDF:** `python scripts/generate_system_prompt_pdf.py`
- **PRD PDF:** `python scripts/generate_prd_pdf.py`
