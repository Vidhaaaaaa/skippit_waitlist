// (function () { const logo = document.getElementById("logo");
//     const whisper = document.getElementById("whisper");
//     let whisperTimer = null;

//     function showWhisper() {
//         if (whisperTimer) clearTimeout(whisperTimer);
//         whisper.style.opacity = 1;
//         whisper.style.transform = "translateX(-50%) translateY(0)";

//         whisperTimer = setTimeout(() => { 
//             whisper.style.opacity = 0;
//             whisper.style.transform = "translateX(-50%) translateY(-6px)";
//         }, 1600);
//     }
    
//     logo.addEventListener("mouseenter", showWhisper);
//     logo.addEventListener("focus", showWhisper);
//     logo.addEventListener("click", showWhisper); 
//     logo.setAttribute("tabindex", "0"); })(); // keyboard focus to show whisper

document.addEventListener('DOMContentLoaded', () => {
  const logo = document.querySelector('.logo-img');
  const whisper = document.getElementById('whisper');

  if (!logo || !whisper) return;

  // Show on hover
  logo.addEventListener('mouseenter', () => {
    whisper.classList.add('show');
  });

  logo.addEventListener('mouseleave', () => {
    whisper.classList.remove('show');
  });

  // Show on click
  logo.addEventListener('click', () => {
    whisper.classList.toggle('show');
  });

  // Show on focus (keyboard navigation)
  logo.addEventListener('focus', () => {
    whisper.classList.add('show');
  });

  logo.addEventListener('blur', () => {
    whisper.classList.remove('show');
  });

  // Make logo focusable with tab
  logo.setAttribute('tabindex', '0');
  logo.setAttribute('role', 'button');
  logo.setAttribute('aria-label', 'skippit logo - made with sleepless nights');
});