/**
 * Chatbot JavaScript - Handles interactions, animations, and API calls for the Iron Lady chatbot.
 * Features: Smooth open/close animations, message handling, and responsive design.
 */
document.addEventListener('DOMContentLoaded', () => {
    // Get DOM elements
    const chatbotIcon = document.getElementById('chatbot-icon');
    const chatbotInterface = document.getElementById('chatbot-interface');
    const chatbotClose = document.getElementById('chatbot-close');
    const chatbotForm = document.getElementById('chatbot-form');
    const chatbotInput = document.getElementById('chatbot-input');
    const chatbotMessages = document.getElementById('chatbot-messages');

    // Toggle chatbot interface with smooth animation
    chatbotIcon.addEventListener('click', () => {
        if (chatbotInterface.classList.contains('hidden')) {
            // Open the chatbot
            chatbotInterface.classList.remove('hidden');
            setTimeout(() => {
                chatbotInterface.classList.add('open'); // Trigger animation
            }, 10); // Small delay to allow DOM update
        } else {
            // Close the chatbot
            chatbotInterface.classList.remove('open');
            setTimeout(() => {
                chatbotInterface.classList.add('hidden'); // Hide after animation
            }, 300); // Match transition duration
        }
        if (chatbotInterface.classList.contains('open')) {
            chatbotInput.focus(); // Focus input when open
        }
    });

    // Close chatbot interface
    chatbotClose.addEventListener('click', () => {
        chatbotInterface.classList.remove('open');
        setTimeout(() => {
            chatbotInterface.classList.add('hidden');
        }, 300);
    });

    /**
     * Append a message to the chat window with appropriate styling.
     * @param {string} sender - 'user-message' or 'bot-message'
     * @param {string} text - The message text
     */
    function appendMessage(sender, text) {
        const messageElem = document.createElement('p');
        messageElem.classList.add(sender);
        messageElem.textContent = text;
        chatbotMessages.appendChild(messageElem);
        // Smooth scroll to bottom
        setTimeout(() => {
            chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
        }, 100);
    }

    // Handle form submission
    chatbotForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const userMessage = chatbotInput.value.trim();
        if (!userMessage) return;

        appendMessage('user-message', userMessage);
        chatbotInput.value = '';

        try {
            // Send message to backend API
            const response = await fetch('/chatbot', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: userMessage }),
            });
            const data = await response.json();
            appendMessage('bot-message', data.response);
        } catch (error) {
            console.error('Error fetching response:', error);
            appendMessage('bot-message', 'Sorry, there was an error. Please try again later.');
        }
    });

    // Optional: Close chatbot on outside click (for better UX)
    document.addEventListener('click', (e) => {
        if (!chatbotInterface.contains(e.target) && !chatbotIcon.contains(e.target) && chatbotInterface.classList.contains('open')) {
            chatbotInterface.classList.remove('open');
            setTimeout(() => {
                chatbotInterface.classList.add('hidden');
            }, 300);
        }
    });
});

// Parallax scrolling effect for background sections
document.addEventListener('scroll', function() {
    const scrolled = window.pageYOffset;
    const parallaxElements = document.querySelectorAll('.parallax');
    parallaxElements.forEach(el => {
        const speed = parseFloat(el.getAttribute('data-speed')) || 0.5;
        el.style.transform = `translateY(${scrolled * speed}px)`;
    });
});
