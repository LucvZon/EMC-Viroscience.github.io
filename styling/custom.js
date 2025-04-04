// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
  console.log("Custom script loaded for target blank."); 

  // Select the specific container for your direct links listing using its ID
  const directLinksContainer = document.querySelector('#direct-links'); 
  
  if (directLinksContainer) {
    console.log("Found #direct-links container.");
    // Find all anchor (<a>) tags *only within* the #direct-links container
    const links = directLinksContainer.querySelectorAll('a'); 
    console.log("Found links inside #direct-links:", links);
    
    links.forEach(link => {
      // Apply target="_blank" ONLY to links within this specific container
      // We can likely assume all links defined manually here are external,
      // but checking href is still safer.
      if (link.href && (link.href.startsWith('http://') || link.href.startsWith('https://'))) {
         console.log("Setting target=_blank for external link in #direct-links:", link.href);
         link.setAttribute('target', '_blank');
         link.setAttribute('rel', 'noopener noreferrer'); // Good practice
      } else {
         console.log("Skipping non-external link in #direct-links:", link.href);
      }
    });
  } else {
      console.log("#direct-links container not found. Target blank logic skipped for this container.");
  }

  // You could add similar blocks here for other listing IDs if needed, 
  // or keep the logic separate as it is now.
});