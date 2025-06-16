window.onload = function () {
  const chat = document.createElement("script");

  chat.src = "https://cdn.jsdelivr.net/npm/rasa-webchat@1.0.1/lib/index.min.js";
  chat.async = true;

  chat.onload = () => {
    window.WebChat.default.init({
      selector: "#chat-container",
      initPayload: "/greet",
      customData: { language: "en" },
      socketUrl: "http://localhost:5005",
      title: "Flight Assistant",
      subtitle: "Book flights easily!",
      inputTextFieldHint: "Type a message...",
      showFullScreenButton: true,
    });
  };

  document.body.appendChild(chat);
};