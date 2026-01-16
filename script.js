// Constants & State
const C_VACUUM = 299792458; // m/s
let C_FIBER = C_VACUUM / 1.4567;
let C_AIR = C_VACUUM / 1.0003;

const MULTIPLIERS = [
    { label: "2x Rep Rate", multiple: 2 },
    { label: "4x Rep Rate", multiple: 4 },
    { label: "8x Rep Rate", multiple: 8 },
    { label: "16x Rep Rate", multiple: 16 },
    { label: "32x Rep Rate", multiple: 32 }
];

function init() {
    calculate();
}

function switchTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));

    // Show selected
    document.getElementById(`${tabName}-tab`).classList.add('active');

    // Find button
    const btns = document.querySelectorAll('.tab-btn');
    if (tabName === 'oscillator') btns[0].classList.add('active');
    else btns[1].classList.add('active');
}

function calculate() {
    // Update Constants from Refractive Index
    const nGlassInput = parseFloat(document.getElementById('n_glass').value);
    const nAirInput = parseFloat(document.getElementById('n_air').value);

    if (!isNaN(nGlassInput) && nGlassInput > 0) {
        C_FIBER = C_VACUUM / nGlassInput;
    }
    if (!isNaN(nAirInput) && nAirInput > 0) {
        C_AIR = C_VACUUM / nAirInput;
    }

    // --- Fiber Calculations ---
    let totalFiberTimeNs = 0;

    // There are 6 fiber segments: fiber_0 to fiber_5
    for (let i = 0; i < 6; i++) {
        const inputEl = document.getElementById(`fiber_${i}`);
        const outEl = document.getElementById(`out_${i}`);

        let valMm = parseFloat(inputEl.value);
        if (isNaN(valMm)) valMm = 0;

        // mm -> m
        const lengthM = valMm / 1000.0;

        // time = distance / speed
        const timeS = lengthM / C_FIBER;
        const timeNs = timeS * 1e9;

        outEl.value = timeNs.toFixed(5);
        totalFiberTimeNs += timeNs;
    }

    document.getElementById('fiber_total').value = totalFiberTimeNs.toFixed(5);

    // --- Free Space Calculations ---
    const fsInput = document.getElementById('fs_input');
    const fsOutput = document.getElementById('fs_output');

    let fsMm = parseFloat(fsInput.value);
    if (isNaN(fsMm)) fsMm = 0;

    const fsM = fsMm / 1000.0;
    const fsTimeS = fsM / C_AIR;
    const fsTimeNs = fsTimeS * 1e9;

    fsOutput.value = fsTimeNs.toFixed(5);

    // --- Totals ---
    const totalCavityTimeNs = totalFiberTimeNs + fsTimeNs;
    document.getElementById('cavity_total').innerText = totalCavityTimeNs.toFixed(5);

    let freqMHz = 0;
    if (totalCavityTimeNs > 0) {
        freqMHz = 1000.0 / totalCavityTimeNs;
    }
    document.getElementById('cavity_freq').innerText = freqMHz.toFixed(3);

    // --- Rep Rate Multiplier Section ---
    renderMultipliers(freqMHz);
}

function renderMultipliers(baseFreqMHz) {
    const container = document.getElementById('multiplier_rows');
    container.innerHTML = '';

    if (baseFreqMHz <= 0) return;

    const baseFreqHz = baseFreqMHz * 1e6;

    MULTIPLIERS.forEach((item, index) => {
        const multiplierVal = 2 * Math.pow(2, index);
        const targetFreqHz = baseFreqHz * multiplierVal;

        // Period = 1 / Freq
        const periodS = 1.0 / targetFreqHz;

        // Distance = Speed * Time
        // Speed = C_FIBER
        const fiberLenM = periodS * C_FIBER;
        const fiberLenMm = fiberLenM * 1000.0;

        const row = document.createElement('div');
        row.className = 'multiplier-row';
        row.innerHTML = `
            <span>${item.label}</span>
            <span>${fiberLenMm.toFixed(3)}</span>
            <span>${(targetFreqHz / 1e6).toFixed(3)}</span>
        `;
        container.appendChild(row);
    });
}

// Initialize on load
document.addEventListener('DOMContentLoaded', init);
