// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
  console.log("Custom script loaded and DOM ready."); // Check 1: Does script start?

  // Try a potentially more specific selector first, then fall back
  // Adjust '#direct-links .quarto-listing-item > a' based on inspecting your HTML
  // Or use the broader '.quarto-listing a' if the structure is standard
  const listingLinks = document.querySelectorAll('#direct-links .quarto-listing-item a, #direct-links a'); // Try targeting links within #direct-links

  console.log("Found links:", listingLinks); // Check 2: Are any links found?

  if (listingLinks.length === 0) {
      console.log("No links found with the current selector. Trying broader selector...");
      // Fallback to the broader selector if the specific one fails
      const broaderLinks = document.querySelectorAll('.quarto-listing a');
      console.log("Found links with broader selector:", broaderLinks);

      broaderLinks.forEach(link => {
         console.log("Checking broader link:", link.href); // Check 3: What links are being processed?
          if (link.href && (link.href.startsWith('http://') || link.href.startsWith('https://'))) {
            console.log("Setting target=_blank for:", link.href); // Check 4: Is it trying to set the attribute?
            link.setAttribute('target', '_blank');
            link.setAttribute('rel', 'noopener noreferrer');
          }
      });

  } else {
       listingLinks.forEach(link => {
         console.log("Checking specific link:", link.href); // Check 3: What links are being processed?
          if (link.href && (link.href.startsWith('http://') || link.href.startsWith('https://'))) {
            console.log("Setting target=_blank for:", link.href); // Check 4: Is it trying to set the attribute?
            link.setAttribute('target', '_blank');
            link.setAttribute('rel', 'noopener noreferrer');
          }
      });
  }
});