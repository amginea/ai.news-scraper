// JavaScript to handle menu clicks & content replacement
document.addEventListener('DOMContentLoaded', () => {
    // Select all menu items
    const menuItems = document.querySelectorAll('.menu-item');
    const contentPlaceholder = document.getElementById('content-placeholder');

    // Content for each menu item
    const contentMap = {
        news: () => `
                    <div class="section-title">News Scraper</div>
                    <p>Enter one or more URLs below (each on a new line) to scrape news articles:</p>
                    <textarea id="news-urls" placeholder="Enter URLs here..."></textarea>
                    <button id="process-urls">Process URLs</button>
                    <p></p>
                    <div class="section-title">Results</div>
                    <div id="results-section" class="results">
                        <div id="results-content">No results available yet.</div>
                    </div>
                `,
        search: () => `
                    <div class="section-title">Search</div>
                    <textarea id="search-input" placeholder="Enter your request here..."></textarea>
                    <button id="search-button">Search</button>
                    <p></p>
                    <div class="section-title">Search results</div>
                    <div id="search-results" class="results-content">
                    </div>
                `
    };

    // Add click event listener to menu items
    menuItems.forEach(item => {
        item.addEventListener('click', () => {
            const contentKey = item.getAttribute('data-content'); // Get the menu item's associated content key
            const selectedContent = contentMap[contentKey](); // Call the function to retrieve content

            // Replace content in the placeholder
            contentPlaceholder.innerHTML = selectedContent;

            if (contentKey === 'search') {
                document.getElementById('search-button').addEventListener('click', async () => {
                    const query = document.getElementById('search-input').value.trim();
                    if (!query) {
                        alert('Please enter a search query.');
                        return;
                    }

                    try {
                        const response = await fetch('http://127.0.0.1:5000/search', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ query })
                        });

                        if (!response.ok) {
                            throw new Error(`Server error: ${response.status}`);
                        }

                        const searchResults = await response.json();
                        const resultsDiv = document.getElementById('search-results');

                        // Render response text as Markdown-like output
                        resultsDiv.innerHTML = searchResults.answer
                    } catch (error) {
                        console.error('Error searching:', error);
                        document.getElementById('search-results').innerText = 'Failed to load search results.';
                    }
                });
            }

            // Add event listener to the "Process URLs" button if on the "News Scraper" page
            if (contentKey === 'news') {
                const processButton = document.getElementById('process-urls');
                processButton.addEventListener('click', async () => {
                    const urls = document
                        .getElementById('news-urls')
                        .value.split('\n')
                        .map(url => url.trim())
                        .filter(url => url !== ''); // Filter out empty lines

                    if (urls.length === 0) {
                        alert('Please enter at least one URL.');
                        return;
                    }

                    try {
                        // Make a POST request to the Flask backend
                        const response = await fetch('http://127.0.0.1:5000/scraper', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify({ urls }), // Send the array of URLs as JSON
                        });

                        if (!response.ok) {
                            throw new Error(`Server error: ${response.status}`);
                        }

                        // Process the response from the backend
                        const result = await response.json();
                        console.log('Response from backend:', result);
                        document.getElementById('results-content').textContent = result.message;
                    } catch (error) {
                        console.error('Error sending URLs to backend:', error);
                        document.getElementById('results-content').innerHTML = 'Failed to process URLs. Please try again later.';
                    }
                });
            }
        });
    });
});