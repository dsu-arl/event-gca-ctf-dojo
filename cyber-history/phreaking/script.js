// script.js

// DTMF frequencies for each button
const dtmfFrequencies = {
    '1': { low: 697, high: 1209 },
    '2': { low: 697, high: 1336 },
    '3': { low: 697, high: 1477 },
    '4': { low: 770, high: 1209 },
    '5': { low: 770, high: 1336 },
    '6': { low: 770, high: 1477 },
    '7': { low: 852, high: 1209 },
    '8': { low: 852, high: 1336 },
    '9': { low: 852, high: 1477 },
    '0': { low: 941, high: 1336 },
    '*': { low: 941, high: 1209 },
    '#': { low: 941, high: 1477 },
    'ringback': { low: 400, high: 450 },
    '2600': { low: 2600, high: 2600 },
    '450': { low: 450, high: 450 },
    '700': { low: 700, high: 700 },
    '1200': { low: 1200, high: 1200 }
};

// Create audio context
const audioContext = new (window.AudioContext || window.webkitAudioContext)();

// Play the DTMF tone for a given key
function playDTMF(key, duration = 0.2) {
    const { low, high } = dtmfFrequencies[key];
    //const duration = 0.2; // Tone duration in seconds

    // Create two oscillators for the DTMF tones
    const oscillatorLow = audioContext.createOscillator();
    const oscillatorHigh = audioContext.createOscillator();

    oscillatorLow.frequency.setValueAtTime(low, audioContext.currentTime);
    oscillatorHigh.frequency.setValueAtTime(high, audioContext.currentTime);

    // Create gain nodes to control volume
    const gainLow = audioContext.createGain();
    const gainHigh = audioContext.createGain();

    gainLow.gain.setValueAtTime(0.5, audioContext.currentTime);
    gainHigh.gain.setValueAtTime(0.5, audioContext.currentTime);

    // Connect the oscillators to the gain nodes and the audio context
    oscillatorLow.connect(gainLow);
    oscillatorHigh.connect(gainHigh);
    gainLow.connect(audioContext.destination);
    gainHigh.connect(audioContext.destination);

    // Start the oscillators
    oscillatorLow.start();
    oscillatorHigh.start();

    // Stop the oscillators after the duration
    oscillatorLow.stop(audioContext.currentTime + duration);
    oscillatorHigh.stop(audioContext.currentTime + duration);
}

// Add event listeners to the keys
document.querySelectorAll('.phone-booth .key').forEach(button => {
    button.addEventListener('click', () => {
        const key = button.getAttribute('data-key');
        playDTMF(key);

        if(key == '#' || key == '*') {
            return;
        }

        let screen = document.querySelector(".screen");
        // Update screen
        if(screen.textContent == "Place a Call") {
            screen.textContent = "";
        }
        screen.textContent += key;

        // if long enough then call
        if(screen.textContent.startsWith("1800") && screen.textContent.length == 11) {
            startRingback();
            screen.textContent = "Calling...";
        } else if(freeCall && screen.textContent == "7552099") {

            fetch("http://127.0.0.1:5000/", {
                method: "POST",
                body: JSON.stringify({
                    verify: `${document.querySelector(".phone-booth").innerHTML}`
                }),
                headers: {
                    "Content-type": "text/plain; charset=UTF-8"
                }
            })
            .then((response) => response.text())
            .then((text) => alert(text));
        }
    });
});

const progression = ['2600', '450', '700', '1200'];
let pi = 0;
let freeCall = false;
document.querySelectorAll('.blue-box .key').forEach(button => {
    button.addEventListener('click', () => {
        const key = button.getAttribute('data-key');
        playDTMF(key);

        if(key == '2600') {
          pi = 1;
          if(isRinging) {
            stopRingback();
            let screen = document.querySelector(".screen")
            screen.textContent = "RESET";
            screen.classList.add("hacked");
          } else {
            return;
          }
          return;
        }

        if(pi < progression.length && key == progression[pi]) {
            pi++;
            display = ""
            if(key == '450') {
                display = "LOCAL CALL";
            } else if(key == '700') {
                display = "ROUTING";
            } else if(key == '1200') {
                display = "Place a Call";
            }
            document.querySelector(".screen").textContent = display;
        } else {
            window.location.reload();
        }

        if(pi >= progression.length) {
            freeCall = true;
        }

    });
});

let ringbackInterval;
let isRinging = false;

function playRingbackTone() {
    playDTMF('ringback', 0.8);
}

function startRingback() {
    if (!isRinging) {
        isRinging = true;
        playRingbackTone();
        ringbackInterval = setInterval(playRingbackTone, 2500);
    }
}

function stopRingback() {
    if (isRinging) {
        isRinging = false;
        clearInterval(ringbackInterval);
    }
}