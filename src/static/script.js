document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('form');
  const loaderContainer = document.getElementById('loader-container');
  const responseContainer = document.getElementById('response-container');
  
  // Hide both containers initially
  loaderContainer.style.display = 'none';
  responseContainer.style.display = 'none';
  responseContainer.innerHTML = '';

  form.addEventListener('submit', async function(e) {
      e.preventDefault();
      
      // Show loader and hide response
      loaderContainer.style.display = 'flex';
      responseContainer.style.display = 'none';
      responseContainer.innerHTML = '';
      
      try {
          const response = await fetch('/', {
              method: 'POST',
              body: new FormData(form),
              headers: {
                  'X-Requested-With': 'XMLHttpRequest' // Identify as AJAX
              }
          });
          
          // Get the raw response text (not HTML)
          const responseText = await response.text();
          
          // Display line by line
          displayResponseLineByLine(responseText);
      } catch (error) {
          console.error('Error:', error);
          responseContainer.innerHTML = '<p>Error processing your request</p>';
          responseContainer.style.display = 'block';
          loaderContainer.style.display = 'none';
      }
  });

  function displayResponseLineByLine(text) {
      responseContainer.style.display = 'block';
      loaderContainer.style.display = 'none';
      responseContainer.innerHTML = '';
      
      // Split by paragraphs (assuming markdown uses \n\n for paragraphs)
      const paragraphs = text.split('\n\n');
      
      let i = 0;
      const interval = setInterval(() => {
          if (i >= paragraphs.length) {
              clearInterval(interval);
              return;
          }
          
          const p = document.createElement('p');
          p.innerHTML = paragraphs[i];
          responseContainer.appendChild(p);
          responseContainer.scrollTop = responseContainer.scrollHeight;
          i++;
      }, 50);
  }
});