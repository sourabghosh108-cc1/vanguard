document.addEventListener('DOMContentLoaded', () => {
  // Live Canvas Audio Frequency Visualizer Animation
  const canvas = document.getElementById('freqCanvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    let width = (canvas.width = canvas.offsetWidth);
    let height = (canvas.height = canvas.offsetHeight);

    window.addEventListener('resize', () => {
      width = (canvas.width = canvas.offsetWidth);
      height = (canvas.height = canvas.offsetHeight);
    });

    let phase = 0;
    function animateWave() {
      ctx.clearRect(0, 0, width, height);
      ctx.beginPath();
      ctx.lineWidth = 2;
      ctx.strokeStyle = '#FF9500';

      const bars = 40;
      const barWidth = width / bars;

      for (let i = 0; i < bars; i++) {
        const barHeight = Math.sin(phase + i * 0.2) * 20 + Math.cos(phase * 1.5 + i * 0.1) * 15 + 30;
        const x = i * barWidth;
        const y = height - barHeight;

        // Draw frequency spectrum line
        ctx.fillStyle = i % 2 === 0 ? '#C87D55' : '#FF9500';
        ctx.fillRect(x + 2, y, barWidth - 4, barHeight);
      }

      phase += 0.05;
      requestAnimationFrame(animateWave);
    }
    animateWave();
  }

  // Interactive Spec Switcher
  const specCards = document.querySelectorAll('.spec-card');
  specCards.forEach(card => {
    card.addEventListener('mouseenter', () => {
      card.style.borderColor = '#FF9500';
    });
    card.addEventListener('mouseleave', () => {
      card.style.borderColor = 'rgba(255, 255, 255, 0.08)';
    });
  });
});
