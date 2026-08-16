/**
 * Whispers of the Wind — AI Voice Agent Interactive Application
 */

// Data definitions for all 5 scenarios
const SCENARIOS = {
  "01-qualified-self-use": {
    id: "01-qualified-self-use",
    title: "Qualified self-use weekend home",
    description: "Prospect seeking a weekend home for his Indiranagar family. Validates permission, intent, geography, budget fit, timeline comfort, delivers the Private Valley pitch, and schedules an expert callback.",
    audioSrc: "assets/audio/01-qualified-self-use.mp3",
    checkpoints: {
      intent: { text: "Self-Use (Weekend Home)", pass: true },
      geography: { text: "Nandi Valley / Airport Corridor", pass: true },
      budget: { text: "₹1.0 – ₹1.5 Cr (Fits ₹92.4L+)", pass: true },
      timeline: { text: "Dec 2029 Delivery Comfortable", pass: true }
    },
    toolCall: {
      name: "schedule_expert_callback",
      payload: {
        caller_name: "Arjun Menon",
        preferred_window: "Tomorrow after 7:00 PM",
        intent: "self_use",
        geography_fit: "yes",
        budget_fit: "yes",
        timeline_fit: "yes",
        language: "en",
        notes: "Indiranagar resident seeking scenic weekend home; impressed by 74% open space density."
      }
    },
    turns: [
      { role: "agent", speaker: "Meera (Divyasree)", voice: "en-IN-NeerjaNeural", text: "Good afternoon. This is Meera, a consultant with Divyaashree Developers. I'm calling about Whispers of the Wind, our private-valley villa-plot community near Nundhee Hills. Do you have a couple of minutes to speak?" },
      { role: "prospect", speaker: "Arjun Menon", voice: "en-IN-PrabhatNeural", text: "Yes, I can talk for a few minutes. What is this regarding?" },
      { role: "agent", speaker: "Meera (Divyasree)", voice: "en-IN-NeerjaNeural", text: "Understood, thank you. It's a private briefing on villa plots in Nundhee Valley. May I ask — were you looking at this more as a weekend home for yourself, or as an investment holding?" },
      { role: "prospect", speaker: "Arjun Menon", voice: "en-IN-PrabhatNeural", text: "Weekend home. We live in Indiranagar and wanted somewhere we can drive out to on Friday evening." },
      { role: "agent", speaker: "Meera (Divyasree)", voice: "en-IN-NeerjaNeural", text: "Perfect. A second home in the hills is exactly how many of our families use it. And the Nundhee Hills, Devanahalli corridor — is that a geography you are comfortable with, rather than a central Bengaluru address?" },
      { role: "prospect", speaker: "Arjun Menon", voice: "en-IN-PrabhatNeural", text: "Yes, we've driven up to Nundhee Hills several times. The air is the point, not being next to the office." },
      { role: "agent", speaker: "Meera (Divyasree)", voice: "en-IN-NeerjaNeural", text: "That makes sense. On fitment — plots here begin at ninety-two point four lakh, going up to about two point four six crore, and that is inclusive of taxes. Is that the band you were considering?" },
      { role: "prospect", speaker: "Arjun Menon", voice: "en-IN-PrabhatNeural", text: "Around a crore to a crore and a half is comfortable for us." },
      { role: "agent", speaker: "Meera (Divyasree)", voice: "en-IN-NeerjaNeural", text: "Understood. That sits well inside the community. One last checkpoint — this is an ongoing, phased project, with possession around December twenty twenty-nine. Are you comfortable holding through that horizon while the valley comes up?" },
      { role: "prospect", speaker: "Arjun Menon", voice: "en-IN-PrabhatNeural", text: "If the land and the master plan are right, twenty twenty-nine is fine. We are not in a rush to build tomorrow." },
      { role: "agent", speaker: "Meera (Divyasree)", voice: "en-IN-NeerjaNeural", text: "Appreciate you sharing that. Whispers of the Wind is designed as a private valley rather than a typical layout. About seventy-four percent of the land stays open — eco-parks, walking greens, and long hill views. At the heart is a twenty-thousand square-foot clubhouse. Plots run from twelve hundred to about thirty-two hundred square feet, so the homes sit in landscape, not on top of each other." },
      { role: "prospect", speaker: "Arjun Menon", voice: "en-IN-PrabhatNeural", text: "That density is what I care about. I don't want another gated grid." },
      { role: "agent", speaker: "Meera (Divyasree)", voice: "en-IN-NeerjaNeural", text: "Then you are looking at the right idea. If it suits you, I will have a property expert call you for a private briefing — no obligation — so you can see inventory in that one-crore band. What time works over the next day or two?" },
      { role: "prospect", speaker: "Arjun Menon", voice: "en-IN-PrabhatNeural", text: "Tomorrow evening after seven. My name is Arjun Menon, this number is fine." },
      { role: "agent", speaker: "Meera (Divyasree)", voice: "en-IN-NeerjaNeural", text: "Perfect, Arjun. I will place you with an expert tomorrow after seven. Thank you for your time — I hope the valley feels like the weekend home you had in mind. I'll let you go." }
    ]
  },
  "02-nri-investment": {
    id: "02-nri-investment",
    title: "Dubai NRI investor, upfront info, ROI query",
    description: "Prospect volunteers intent, geography, and ₹2 Cr budget in turn 1. Agent avoids redundant re-asking, answers low-density inquiry, deflects ROI projection professionally without inventing yields, and books weekend video consultation.",
    audioSrc: "assets/audio/02-nri-investment.mp3",
    checkpoints: {
      intent: { text: "Investment (Long-Term Land Hold)", pass: true },
      geography: { text: "Nandi / Devanahalli Corridor", pass: true },
      budget: { text: "₹2.0 Crore Band (Fits ₹92.4L+)", pass: true },
      timeline: { text: "Dec 2029 Delivery Comfortable", pass: true }
    },
    toolCall: {
      name: "schedule_expert_callback",
      payload: {
        caller_name: "Kabir Shah",
        preferred_window: "This weekend (Dubai evening)",
        intent: "investment",
        geography_fit: "yes",
        budget_fit: "yes",
        timeline_fit: "yes",
        language: "en",
        notes: "Dubai NRI looking for long-term land hold in airport corridor (~2 Cr band). Requested private video walkthrough."
      }
    },
    turns: [
      { role: "agent", speaker: "Meera (Divyasree)", voice: "en-IN-NeerjaNeural", text: "Good evening. This is Meera, a consultant with Divyaashree Developers. I'm calling about Whispers of the Wind, our private-valley villa-plot community near Nundhee Hills. Do you have a couple of minutes to speak?" },
      { role: "prospect", speaker: "Kabir Shah", voice: "en-IN-PrabhatNeural", text: "I can talk. I'm based in Dubai, looking at land in North Bengaluru as a long-term hold, budget around two crore. Nundhee, Devanahalli is fine — I already know that corridor from the airport." },
      { role: "agent", speaker: "Meera (Divyasree)", voice: "en-IN-NeerjaNeural", text: "Understood — an N-R-I holding in the Nundhee, Devanahalli corridor, around two crore. I will not take you back over that. The only checkpoint I still need is timeline. This is a phased, ongoing project, with possession around December twenty twenty-nine. Are you comfortable with that horizon?" },
      { role: "prospect", speaker: "Kabir Shah", voice: "en-IN-PrabhatNeural", text: "For land, yes. I am not buying a ready apartment. What I need to understand is whether this is actually low density, or marketing language." },
      { role: "agent", speaker: "Meera (Divyasree)", voice: "en-IN-NeerjaNeural", text: "Fair question. Seventy-four percent of the land is kept open — eco-parks and long views to the hills. Plots are twelve hundred to about thirty-two hundred square feet, so you are buying a private valley plot, not a tight row house pad. The twenty-thousand square-foot clubhouse is for residents, not a public resort. Pricing for that two-crore band is inside the published range of ninety-two point four lakh to two point four six crore, taxes included." },
      { role: "prospect", speaker: "Kabir Shah", voice: "en-IN-PrabhatNeural", text: "And the yield? What do your investors typically make?" },
      { role: "agent", speaker: "Meera (Divyasree)", voice: "en-IN-NeerjaNeural", text: "We do not project returns on this call, and I will not quote a number I cannot stand behind. Clients usually weigh it as a long-horizon land holding in the airport-led North Bengaluru corridor. A property expert can share corridor context — not a guaranteed yield." },
      { role: "prospect", speaker: "Kabir Shah", voice: "en-IN-PrabhatNeural", text: "That's a better answer than most people give me. All right. Can someone walk me through inventory on a video call this weekend? I'm Kabir Shah." },
      { role: "agent", speaker: "Meera (Divyasree)", voice: "en-IN-NeerjaNeural", text: "Of course, Kabir. I will have a property expert set a private video briefing this weekend, around your Dubai evening. They will stay with facts — inventory, plot sizes, and the December twenty twenty-nine delivery. Thank you for your time. I'll leave you to your evening." }
    ]
  },
  "03-budget-fit-location-mismatch": {
    id: "03-budget-fit-location-mismatch",
    title: "Budget fits, location does not (City Commuter)",
    description: "Prospect has strong purchasing power (₹2 Cr) but needs daily commute to Whitefield/city core. Meera respects the commute constraint without arguing and exits gracefully.",
    audioSrc: "assets/audio/03-budget-fit-location-mismatch.mp3",
    checkpoints: {
      intent: { text: "Self-Use (Primary Home)", pass: true },
      geography: { text: "Mismatch (Requires Whitefield Core)", pass: false },
      budget: { text: "₹2.0 Crore (Comfortable)", pass: true },
      timeline: { text: "Unsure / Commute Constraint", pass: false }
    },
    toolCall: {
      name: "log_outcome",
      payload: {
        outcome: "location_mismatch",
        intent: "self_use",
        notes: "Lead has ₹2 Cr budget but requires daily commute to Whitefield. Respectfully disqualified from Nandi Valley outreach."
      }
    },
    turns: [
      { role: "agent", speaker: "Meera (Divyasree)", voice: "en-IN-NeerjaNeural", text: "Good afternoon. This is Meera, a consultant with Divyaashree Developers. I'm calling about Whispers of the Wind, near Nundhee Hills. Do you have a couple of minutes to speak?" },
      { role: "prospect", speaker: "Prospect", voice: "en-IN-PrabhatNeural", text: "Go on. I was looking at villa plots, but I assumed something closer in — Whitefield or Sarjapur." },
      { role: "agent", speaker: "Meera (Divyasree)", voice: "en-IN-NeerjaNeural", text: "Understood. This one sits in Nundhee Valley, on the Nundhee Hills, Devanahalli corridor, not in Whitefield. Were you looking at a home for yourselves, or more as an investment?" },
      { role: "prospect", speaker: "Prospect", voice: "en-IN-PrabhatNeural", text: "For us. We want to move out of an apartment over the next few years. Budget is not the issue — we can do up to two crore." },
      { role: "agent", speaker: "Meera (Divyasree)", voice: "en-IN-NeerjaNeural", text: "Perfect, that band fits. Plots here begin at ninety-two point four lakh and go to about two point four six crore, taxes included. The open question is geography. Nundhee is a highland weekend and second-home landscape, not a city neighbourhood. How do you feel about that corridor?" },
      { role: "prospect", speaker: "Prospect", voice: "en-IN-PrabhatNeural", text: "Honestly, too far. I still come into the city four days a week. I don't want a two-hour mistake." },
      { role: "agent", speaker: "Meera (Divyasree)", voice: "en-IN-NeerjaNeural", text: "That is a fair read, and I will not talk you past it. This valley is meant for people who want the hills, the seventy-four percent open space, and a slower weekend — not a weekday commute. If the location still feels off, I will not push." },
      { role: "prospect", speaker: "Prospect", voice: "en-IN-PrabhatNeural", text: "I appreciate that. If you had something inside the outer ring I would listen. This one is not for me." },
      { role: "agent", speaker: "Meera (Divyasree)", voice: "en-IN-NeerjaNeural", text: "Understood. I will not set a visit. Thank you for being direct — it saves both of us a drive. I hope you find a plot that sits closer to the life you already have. I'll let you go." }
    ]
  },
  "04-irritated-user": {
    id: "04-irritated-user",
    title: "Irritated caller, do-not-contact / DND",
    description: "Caller in a meeting / irritated with sales calls. Meera immediately offers an exit, caller requests DND, Meera logs do_not_contact, apologizes, and ends call.",
    audioSrc: "assets/audio/04-irritated-user.mp3",
    checkpoints: {
      intent: { text: "Unknown", pass: false },
      geography: { text: "Unknown", pass: false },
      budget: { text: "Unknown", pass: false },
      timeline: { text: "Unknown", pass: false }
    },
    toolCall: {
      name: "log_outcome",
      payload: {
        outcome: "do_not_contact",
        notes: "Prospect requested immediate removal from calling list during meeting. DND logged; suppressed from all future campaigns."
      }
    },
    turns: [
      { role: "agent", speaker: "Meera (Divyasree)", voice: "en-IN-NeerjaNeural", text: "Good afternoon. This is Meera, a consultant with Divyaashree Developers. I'm calling about Whispers of the Wind, near Nundhee Hills. Do you have a couple of minutes to speak?" },
      { role: "prospect", speaker: "Prospect", voice: "en-IN-PrabhatNeural", text: "How did you get this number? I am in a meeting. You people keep calling." },
      { role: "agent", speaker: "Meera (Divyasree)", voice: "en-IN-NeerjaNeural", text: "I'm sorry to have caught you at a bad time. I'll let you go." },
      { role: "prospect", speaker: "Prospect", voice: "en-IN-PrabhatNeural", text: "Don't just let me go. Take me off your list. I do not want another real-estate call." },
      { role: "agent", speaker: "Meera (Divyasree)", voice: "en-IN-NeerjaNeural", text: "Understood. I will note that you do not wish to be contacted again. I am sorry for the interruption. Goodbye." }
    ]
  },
  "05-hindi-english": {
    id: "05-hindi-english",
    title: "Hindi / Hinglish code-switch, fully qualified",
    description: "Prospect requests Hindi. Meera smoothly code-switches to natural conversational Hindi with authentic Indian real estate terms, completes qualification, and books callback.",
    audioSrc: "assets/audio/05-hindi-english.mp3",
    checkpoints: {
      intent: { text: "Both (Family Second Home + Investment)", pass: true },
      geography: { text: "Comfortable (Looking Airport Side)", pass: true },
      budget: { text: "₹1.0 Cr Comfortable (Fits ₹92.4L+)", pass: true },
      timeline: { text: "Dec 2029 Phased Comfortable", pass: true }
    },
    toolCall: {
      name: "schedule_expert_callback",
      payload: {
        caller_name: "Rohan Gupta",
        preferred_window: "Kal shaam (Tomorrow evening)",
        intent: "both",
        geography_fit: "yes",
        budget_fit: "yes",
        timeline_fit: "yes",
        language: "hi",
        notes: "Hindi preference. Second home + investment in ~1 Cr band. Private briefing arranged for him and his spouse."
      }
    },
    turns: [
      { role: "agent", speaker: "Meera (Divyasree)", voice: "hi-IN-SwaraNeural", text: "Namaste, main Meera bol rahi hoon, Divyaashree Developers se. Whispers of the Wind ke baare mein call kiya hai — Nundhee Hills ke paas private valley villa plots. Kya aap do minute baat kar sakte hain?" },
      { role: "prospect", speaker: "Rohan Gupta", voice: "hi-IN-MadhurNeural", text: "Haan, boliye. Main Hindi mein theek hoon. Ye project kahan hai exactly?" },
      { role: "agent", speaker: "Meera (Divyasree)", voice: "hi-IN-SwaraNeural", text: "Nundhee Valley, Nundhee Hills ke paas, North Bengaluru. Devanahalli corridor. Pehle ye poochh loon — aap khud ke weekend ghar ke liye dekh rahe hain, ya investment ke liye?" },
      { role: "prospect", speaker: "Rohan Gupta", voice: "hi-IN-MadhurNeural", text: "Dono. Family ke liye second home, aur agar value bane to theek hai. Location se problem nahi, hum airport side pehle se dekh rahe hain." },
      { role: "agent", speaker: "Meera (Divyasree)", voice: "hi-IN-SwaraNeural", text: "Samajh gayi. Geography theek hai. Budget ke baare mein — yahan plots ninety-two point four lakh se shuru hote hain, takriban two point four six crore tak, tax included. Kya yahi range aap dekh rahe hain?" },
      { role: "prospect", speaker: "Rohan Gupta", voice: "hi-IN-MadhurNeural", text: "Haan, one crore ke around comfortable hai. Possession kab ka hai? Ready to move to nahi hoga na?" },
      { role: "agent", speaker: "Meera (Divyasree)", voice: "hi-IN-SwaraNeural", text: "Sahi pakda. Ye ongoing, phased project hai. Possession December twenty twenty-nine ke around hai. Ready villa nahi milti — aap plot lete hain, ghar baad mein guidelines pe banate hain. Is horizon se aap comfortable hain?" },
      { role: "prospect", speaker: "Rohan Gupta", voice: "hi-IN-MadhurNeural", text: "Haan, jaldi nahi hai. Thoda batao community kaisi hai." },
      { role: "agent", speaker: "Meera (Divyasree)", voice: "hi-IN-SwaraNeural", text: "Whispers of the Wind ek private valley ki tarah socha gaya hai, typical layout ki tarah nahi. Chhahattar percent zameen open rehti hai — eco-parks, walking greens, aur hills ke views. Beech mein bees hazaar square feet ka clubhouse hai. Plots twelve hundred se lagbhag thirty-two hundred square feet tak hain, isliye ghar landscape ke andar baithe hain, ek doosre ke upar nahi." },
      { role: "prospect", speaker: "Rohan Gupta", voice: "hi-IN-MadhurNeural", text: "Achha lagta hai. Koi expert se baat ho sakti hai? Meri wife bhi sunna chahegi. Kal shaam theek rahegi. Mera naam Rohan Gupta hai." },
      { role: "agent", speaker: "Meera (Divyasree)", voice: "hi-IN-SwaraNeural", text: "Bilkul, Rohan. Kal shaam property expert aap dono se private call karenge — koi pressure nahi. Aapka time dene ke liye dhanyavaad. Main aapko ab leave karti hoon." }
    ]
  }
};

let currentScenarioId = "01-qualified-self-use";
const audioPlayer = document.getElementById("mainAudioPlayer");
const btnPlayPause = document.getElementById("btnPlayPause");
const iconPlay = document.getElementById("iconPlay");
const iconPause = document.getElementById("iconPause");
const currentTimeEl = document.getElementById("currentTime");
const totalDurationEl = document.getElementById("totalDuration");
const timelineSlider = document.getElementById("timelineSlider");
const timelineProgressBar = document.getElementById("timelineProgressBar");
const playbackSpeedSelect = document.getElementById("playbackSpeed");

function formatTime(seconds) {
  if (isNaN(seconds)) return "0:00";
  const mins = Math.floor(seconds / 60);
  const secs = Math.floor(seconds % 60);
  return `${mins}:${secs < 10 ? '0' : ''}${secs}`;
}

function loadScenario(scenarioId) {
  currentScenarioId = scenarioId;
  const scenario = SCENARIOS[scenarioId];
  if (!scenario) return;

  // Update tabs UI
  document.querySelectorAll(".scenario-tab-btn").forEach(btn => {
    btn.classList.toggle("active", btn.dataset.scenario === scenarioId);
  });

  // Update meta
  document.getElementById("activeScenarioTitle").textContent = scenario.title;
  document.getElementById("activeScenarioDesc").textContent = scenario.description;
  document.getElementById("btnDownloadMp3").href = scenario.audioSrc;
  document.getElementById("turnCountBadge").textContent = `${scenario.turns.length} Spoken Turns`;

  // Update Checkpoints
  const cpIntent = document.getElementById("cpIntent");
  const cpGeo = document.getElementById("cpGeo");
  const cpBudget = document.getElementById("cpBudget");
  const cpTimeline = document.getElementById("cpTimeline");

  document.getElementById("cpIntentStatus").textContent = scenario.checkpoints.intent.text;
  document.getElementById("cpGeoStatus").textContent = scenario.checkpoints.geography.text;
  document.getElementById("cpBudgetStatus").textContent = scenario.checkpoints.budget.text;
  document.getElementById("cpTimelineStatus").textContent = scenario.checkpoints.timeline.text;

  cpIntent.className = `checkpoint-item ${scenario.checkpoints.intent.pass ? 'status-pass' : 'status-fail'}`;
  cpGeo.className = `checkpoint-item ${scenario.checkpoints.geography.pass ? 'status-pass' : 'status-fail'}`;
  cpBudget.className = `checkpoint-item ${scenario.checkpoints.budget.pass ? 'status-pass' : 'status-fail'}`;
  cpTimeline.className = `checkpoint-item ${scenario.checkpoints.timeline.pass ? 'status-pass' : 'status-fail'}`;

  // Update Tool Card
  document.getElementById("emittedToolName").textContent = scenario.toolCall.name;
  document.getElementById("emittedToolJson").textContent = JSON.stringify(scenario.toolCall.payload, null, 2);

  // Render Transcript Turns
  const streamEl = document.getElementById("transcriptStream");
  streamEl.innerHTML = "";

  scenario.turns.forEach((turn, idx) => {
    const isAgent = turn.role === "agent";
    const turnEl = document.createElement("div");
    turnEl.className = "transcript-turn";
    turnEl.dataset.turnIndex = idx;

    turnEl.innerHTML = `
      <div class="turn-avatar ${isAgent ? 'avatar-agent' : 'avatar-prospect'}">
        ${isAgent ? 'M' : 'P'}
      </div>
      <div class="turn-body">
        <div class="turn-meta">
          <span class="turn-speaker">${turn.speaker}</span>
          <span class="turn-voice">${turn.voice}</span>
        </div>
        <div class="turn-text">${turn.text}</div>
      </div>
    `;

    // Click turn to jump to approx time
    turnEl.addEventListener("click", () => {
      if (audioPlayer.duration) {
        const turnFraction = idx / scenario.turns.length;
        audioPlayer.currentTime = turnFraction * audioPlayer.duration;
        audioPlayer.play();
        updatePlayPauseUI(true);
      }
    });

    streamEl.appendChild(turnEl);
  });

  // Load Audio
  audioPlayer.src = scenario.audioSrc;
  audioPlayer.load();
  updatePlayPauseUI(false);
}

function updatePlayPauseUI(isPlaying) {
  if (isPlaying) {
    iconPlay.style.display = "none";
    iconPause.style.display = "block";
  } else {
    iconPlay.style.display = "block";
    iconPause.style.display = "none";
  }
}

// Audio Player Events
btnPlayPause.addEventListener("click", () => {
  if (audioPlayer.paused) {
    audioPlayer.play();
    updatePlayPauseUI(true);
  } else {
    audioPlayer.pause();
    updatePlayPauseUI(false);
  }
});

audioPlayer.addEventListener("timeupdate", () => {
  const current = audioPlayer.currentTime;
  const duration = audioPlayer.duration || 1;
  currentTimeEl.textContent = formatTime(current);
  timelineSlider.value = (current / duration) * 100;

  // Highlight active turn proportionally
  const turns = document.querySelectorAll(".transcript-turn");
  if (turns.length > 0) {
    const activeIndex = Math.min(
      Math.floor((current / duration) * turns.length),
      turns.length - 1
    );
    turns.forEach((t, i) => {
      t.classList.toggle("active-turn", i === activeIndex);
    });
  }
});

audioPlayer.addEventListener("loadedmetadata", () => {
  totalDurationEl.textContent = formatTime(audioPlayer.duration);
});

audioPlayer.addEventListener("ended", () => {
  updatePlayPauseUI(false);
  timelineSlider.value = 100;
});

timelineSlider.addEventListener("input", (e) => {
  if (audioPlayer.duration) {
    audioPlayer.currentTime = (e.target.value / 100) * audioPlayer.duration;
  }
});

playbackSpeedSelect.addEventListener("change", (e) => {
  audioPlayer.playbackRate = parseFloat(e.target.value);
});

// Scenario Tab Click Handlers
document.querySelectorAll(".scenario-tab-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    loadScenario(btn.dataset.scenario);
  });
});

// Download JSON Transcript Handler
document.getElementById("btnDownloadTranscript").addEventListener("click", () => {
  const scenario = SCENARIOS[currentScenarioId];
  const blob = new Blob([JSON.stringify(scenario, null, 2)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `${currentScenarioId}-transcript.json`;
  a.click();
  URL.revokeObjectURL(url);
});

// ==========================================================================
// Live Interactive Bot Simulator Engine
// ==========================================================================

const simState = {
  stage: 0,
  permission: true,
  intent: null,
  geography: null,
  budget: null,
  timeline: null,
  language: "en",
  disqualified: false,
  callerName: "Prospective Buyer"
};

const simMessagesStream = document.getElementById("simMessagesStream");
const simInputForm = document.getElementById("simInputForm");
const simInputText = document.getElementById("simInputText");
const chkSimAudio = document.getElementById("chkSimAudio");
const btnResetSim = document.getElementById("btnResetSim");

function speakTTS(text, lang = "en-IN") {
  if (!chkSimAudio.checked || !window.speechSynthesis) return;
  window.speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.rate = 1.0;
  utterance.lang = lang === "hi" ? "hi-IN" : "en-IN";
  window.speechSynthesis.speak(utterance);
}

function appendSimMessage(role, text) {
  const bubble = document.createElement("div");
  bubble.className = `sim-bubble ${role === "agent" ? 'sim-bubble-agent' : 'sim-bubble-user'}`;
  bubble.textContent = text;
  simMessagesStream.appendChild(bubble);
  simMessagesStream.scrollTop = simMessagesStream.scrollHeight;

  if (role === "agent") {
    speakTTS(text, simState.language);
  }
}

function updateSimStateUI() {
  document.getElementById("simStateIntent").textContent = simState.intent || "Pending";
  document.getElementById("simStateIntent").className = `meter-val ${simState.intent ? 'val-green' : ''}`;

  document.getElementById("simStateGeo").textContent = simState.geography || "Pending";
  document.getElementById("simStateGeo").className = `meter-val ${simState.geography === 'Fit (Nandi)' ? 'val-green' : (simState.geography ? 'val-red' : '')}`;

  document.getElementById("simStateBudget").textContent = simState.budget || "Pending";
  document.getElementById("simStateBudget").className = `meter-val ${simState.budget ? 'val-green' : ''}`;

  document.getElementById("simStateTimeline").textContent = simState.timeline || "Pending";
  document.getElementById("simStateTimeline").className = `meter-val ${simState.timeline ? 'val-green' : ''}`;

  document.getElementById("simStateLang").textContent = simState.language === "hi" ? "Hindi (hi-IN)" : "English (en-IN)";

  const toolBox = document.getElementById("simToolEmittedBox");
  if (simState.disqualified) {
    toolBox.innerHTML = `<strong>Tool: log_outcome</strong><br>${JSON.stringify({
      outcome: simState.disqualified,
      intent: simState.intent || "unknown",
      notes: "Lead disqualified gracefully based on fitment / DND criteria."
    }, null, 2)}`;
  } else if (simState.intent && simState.geography === "Fit (Nandi)" && simState.budget && simState.timeline) {
    toolBox.innerHTML = `<strong>Tool: schedule_expert_callback</strong><br>${JSON.stringify({
      caller_name: simState.callerName,
      preferred_window: "Tomorrow evening",
      intent: simState.intent,
      geography_fit: "yes",
      budget_fit: "yes",
      timeline_fit: "yes",
      language: simState.language
    }, null, 2)}`;
  }
}

function processUserInput(input) {
  const text = input.trim();
  if (!text) return;

  appendSimMessage("user", text);
  simInputText.value = "";

  const lower = text.toLowerCase();

  // 1. Language Detection
  if (lower.includes("hindi") || lower.includes("namaste") || lower.includes("boliye") || lower.includes("baat karo") || lower.includes("kahan hai")) {
    simState.language = "hi";
  }

  // 2. DND / Irritated Caller Handling
  if (lower.includes("meeting") || lower.includes("stop calling") || lower.includes("remove me") || lower.includes("don't call") || lower.includes("dnd") || lower.includes("irritated")) {
    simState.disqualified = "do_not_contact";
    updateSimStateUI();
    setTimeout(() => {
      appendSimMessage("agent", "Understood. I will note that you do not wish to be contacted again. I sincerely apologize for the interruption. Goodbye.");
    }, 500);
    return;
  }

  // 3. Location Mismatch Detection
  if (lower.includes("whitefield") || lower.includes("sarjapur") || lower.includes("electronic city") || lower.includes("too far") || lower.includes("daily commute")) {
    simState.geography = "Mismatch (Core City)";
    simState.disqualified = "location_mismatch";
    if (lower.includes("weekend") || lower.includes("second home")) simState.intent = "Self-Use";
    if (lower.includes("crore") || lower.includes("cr") || lower.includes("lakh")) simState.budget = "Comfortable (₹1Cr+)";
    updateSimStateUI();
    setTimeout(() => {
      appendSimMessage("agent", "That is a fair read, and I will not talk you past it. Whispers of the Wind is meant for people looking for a hillside weekend retreat and open spaces, not a daily city commute. Thank you for being direct — I hope you find a property closer to your daily routine.");
    }, 600);
    return;
  }

  // 4. Extract Multi-Entities Upfront (No redundant re-asking)
  if (lower.includes("weekend") || lower.includes("second home") || lower.includes("myself") || lower.includes("family")) {
    simState.intent = "Self-Use (Weekend Home)";
  } else if (lower.includes("invest") || lower.includes("roi") || lower.includes("yield") || lower.includes("nri") || lower.includes("dubai")) {
    simState.intent = "Investment";
  }

  if (lower.includes("nandi") || lower.includes("devanahalli") || lower.includes("airport") || lower.includes("north bangalore")) {
    simState.geography = "Fit (Nandi)";
  }

  if (lower.includes("crore") || lower.includes("cr") || lower.includes("lakh") || lower.includes("1.2") || lower.includes("1.5") || lower.includes("2")) {
    simState.budget = "Fit (₹92.4L – ₹2.46Cr)";
  }

  if (lower.includes("2029") || lower.includes("phased") || lower.includes("ready") || lower.includes("fine") || lower.includes("not in a rush")) {
    simState.timeline = "Comfortable (Dec 2029)";
  }

  updateSimStateUI();

  // Generate Next Contextual Agent Response
  setTimeout(() => {
    let reply = "";

    if (simState.language === "hi") {
      if (!simState.intent) {
        reply = "Namaste. Main Divyaashree Developers se Meera bol rahi hoon. Nundhee Hills ke paas Whispers of the Wind ke baare mein private briefing hai. Kya aap weekend ghar ke liye dekh rahe hain, ya investment ke liye?";
      } else if (!simState.budget) {
        reply = "Samajh gayi. Yahan plots ninety-two point four lakh se shuru hote hain, takriban two point four six crore tak. Kya ye budget band comfortable hai?";
      } else if (!simState.timeline) {
        reply = "Ye ongoing, phased project hai jiska possession December twenty twenty-nine ke around hai. Kya is delivery horizon se aap comfortable hain?";
      } else {
        reply = "Whispers of the Wind mein chhahattar percent open space, eco-parks aur bees hazaar square feet ka clubhouse hai. Kal shaam kya hamare property expert aapko call kar sakte hain?";
      }
    } else {
      // English Mode Logic
      if (lower.includes("roi") || lower.includes("yield") || lower.includes("returns")) {
        reply = "We do not project returns on this call, and I will not quote a number I cannot stand behind. Clients usually evaluate this as a long-horizon land holding in the high-growth airport corridor. A property expert can share corridor trends without making speculative promises.";
        simState.intent = "Investment";
        simState.geography = "Fit (Nandi)";
        simState.budget = "Fit (₹2.0 Cr)";
        simState.timeline = "Comfortable (Dec 2029)";
      } else if (!simState.intent) {
        reply = "Understood, thank you. May I ask — were you looking at this more as a weekend home for yourself, or as an investment holding?";
      } else if (!simState.geography) {
        reply = "Perfect. And is the Nundhee Hills and Devanahalli corridor a geography you are comfortable exploring for this?";
      } else if (!simState.budget) {
        reply = "On fitment — plots at Whispers of the Wind begin at ninety-two point four lakh and go up to two point four six crore, inclusive of taxes. Is that the band you had in mind?";
      } else if (!simState.timeline) {
        reply = "One last checkpoint — this is an ongoing phased development with possession targeted for December twenty twenty-nine. Are you comfortable holding through that horizon?";
      } else {
        reply = "Whispers of the Wind is designed as a low-density private valley with seventy-four percent open spaces, eco-parks, and a twenty-thousand square-foot clubhouse. If it suits you, I will have a Property Expert arrange a private video briefing over the next couple of days. What time works best?";
      }
    }

    appendSimMessage("agent", reply);
    updateSimStateUI();
  }, 600);
}

simInputForm.addEventListener("submit", (e) => {
  e.preventDefault();
  processUserInput(simInputText.value);
});

btnResetSim.addEventListener("click", () => {
  simMessagesStream.innerHTML = "";
  simState.stage = 0;
  simState.permission = true;
  simState.intent = null;
  simState.geography = null;
  simState.budget = null;
  simState.timeline = null;
  simState.language = "en";
  simState.disqualified = false;
  updateSimStateUI();
  document.getElementById("simToolEmittedBox").innerHTML = `<span class="text-muted">Awaiting completion of qualification checkpoints...</span>`;
  
  appendSimMessage("agent", "Good afternoon. This is Meera, a consultant with Divyaashree Developers. I'm calling about Whispers of the Wind, our private-valley villa-plot community near Nundhee Hills. Do you have a couple of minutes to speak?");
});

// Quick Prompt Chips
document.querySelectorAll(".btn-prompt-chip").forEach(chip => {
  chip.addEventListener("click", () => {
    processUserInput(chip.dataset.text);
  });
});

// ==========================================================================
// System Prompt & Navigation Tabs
// ==========================================================================

document.querySelectorAll(".prompt-nav-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".prompt-nav-btn").forEach(b => b.classList.remove("active"));
    document.querySelectorAll(".prompt-tab-pane").forEach(p => p.classList.remove("active"));
    btn.classList.add("active");
    document.getElementById(btn.dataset.target).classList.add("active");
  });
});

// Copy Buttons
document.querySelectorAll(".btn-copy").forEach(btn => {
  btn.addEventListener("click", () => {
    const targetId = btn.dataset.copy;
    const text = document.getElementById(targetId).textContent;
    navigator.clipboard.writeText(text).then(() => {
      const orig = btn.textContent;
      btn.textContent = "Copied!";
      setTimeout(() => btn.textContent = orig, 1800);
    });
  });
});

// Smooth Scroll for Nav Links
document.querySelectorAll(".nav-links a[href^='#']").forEach(link => {
  link.addEventListener("click", (e) => {
    e.preventDefault();
    const target = document.querySelector(link.getAttribute("href"));
    if (target) {
      target.scrollIntoView({ behavior: "smooth" });
    }
  });
});

// Initialize on Load
window.addEventListener("DOMContentLoaded", () => {
  loadScenario("01-qualified-self-use");
  appendSimMessage("agent", "Good afternoon. This is Meera, a consultant with Divyaashree Developers. I'm calling about Whispers of the Wind, our private-valley villa-plot community near Nundhee Hills. Do you have a couple of minutes to speak?");
});
