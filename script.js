// Constants & State
let C_FIBER = 205802470;
let C_AIR = 299702547;

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
    if(tabName === 'oscillator') btns[0].classList.add('active');
    else btns[1].classList.add('active');
}

function calculate() {
    // Update Constants
    const cFiberInput = parseFloat(document.getElementById('c_fiber').value);
    const cAirInput = parseFloat(document.getElementById('c_air').value);
    
    if (!isNaN(cFiberInput)) C_FIBER = cFiberInput;
    if (!isNaN(cAirInput)) C_AIR = cAirInput;

    // --- Fiber Calculations ---
    let totalFiberTimeNs = 0;
    
    // There are 6 fiber segments: fiber_0 to fiber_5
    for (let i = 0; i < 6; i++) {
        const inputEl = document.getElementById(`fiber_${i}`);
        const outEl = document.getElementById(`out_${i}`);
        
        let valCm = parseFloat(inputEl.value);
        if (isNaN(valCm)) valCm = 0;

        // cm -> m
        const lengthM = valCm / 100.0;
        
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
    
    let fsCm = parseFloat(fsInput.value);
    if (isNaN(fsCm)) fsCm = 0;

    const fsM = fsCm / 100.0;
    const fsTimeS = fsM / C_AIR;
    const fsTimeNs = fsTimeS * 1e9;

    fsOutput.value = fsTimeNs.toFixed(5);

    // --- Totals ---
    const totalCavityTimeNs = totalFiberTimeNs + fsTimeNs;
    document.getElementById('cavity_total').innerText = totalCavityTimeNs.toFixed(5);

    let freqMHz = 0;
    if (totalCavityTimeNs > 0) {
        // Frequency = 1 / Period. Period is in ns (1e-9), so 1/ns = GHz. *1000 = MHz.
        // Actually: 1 / (T_ns * 10^-9) = 10^9 / T_ns Hz = 10^3 / T_ns MHz
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
        // Real multiplier is 2 * (2^index) -> 2, 4, 8, 16... wait, let's check python code
        // Python: mult = 2 * (2**i) -> i=0 -> 2, i=1 -> 4, i=2 -> 8
        // My array matches this logic.
        
        const multiplierVal = 2 * Math.pow(2, index); 
        const targetFreqHz = baseFreqHz * multiplierVal;
        
        // Calculate required fiber length for this freq
        // Period = 1 / Freq
        const periodS = 1.0 / targetFreqHz;
        
        // Distance = Speed * Time
        // Speed = C_FIBER
        const fiberLenM = periodS * C_FIBER;
        const fiberLenCm = fiberLenM * 100.0;

        const row = document.createElement('div');
        row.className = 'multiplier-row';
        row.innerHTML = `
            <span>${item.label}</span>
            <span>${fiberLenCm.toFixed(3)}</span>
            <span>${(targetFreqHz / 1e6).toFixed(3)}</span>
        `;
        container.appendChild(row);
    });
}

// Initialize on load
document.addEventListener('DOMContentLoaded', init);
