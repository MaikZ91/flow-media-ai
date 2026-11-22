/* 7 Days AI Challenge – everything Maik may want to change lives here. */
window.CHALLENGE = {
  start: "2026-11-30T00:00:00+01:00",   // Challenge start (Berlin)
  ende: "2026-12-06T23:59:00+01:00",

  // WhatsApp group of the challenge. Shown only on danke.html (after booking), never on the public page.
  whatsappChallenge: "",

  // Maik's WhatsApp number (for bookings as long as no payment link is set)
  whatsappMaik: "4917645961547",

  // Payment links per package (e.g. Stripe Payment Link, PayPal.me, Digistore).
  // Empty = the booking is sent to Maik via WhatsApp and he sends the payment link himself.
  // Stripe: set the success URL of the payment link to …/marketing/challenge/danke.html
  zahlung: {
    starter: "",
    premium: "",
    intensive: "",
  },

  community: "../community/",
};
