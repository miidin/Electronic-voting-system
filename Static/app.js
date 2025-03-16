// Function to request OTP
function sendOTP() {
    let phone = document.getElementById("phone").value;
    fetch("/send-otp", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ phone: phone })
    }).then(response => response.json()).then(data => {
        alert(data.message); // Show OTP sent confirmation
    });
}

// Function to verify OTP
function verifyOTP() {
    let otp = document.getElementById("otp").value;
    fetch("/verify-otp", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ otp: otp })
    }).then(response => response.json()).then(data => {
        if (data.success) {
            alert("OTP Verified! Proceed to vote.");
            window.location.href = "/vote";
        } else {
            alert("Invalid OTP. Try again.");
        }
    });
}
