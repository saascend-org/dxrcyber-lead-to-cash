# DXR Cyber lead-to-cash map

Password-gated interactive map of how a deal flows across Salesforce, Halo and Business Central.

- Live: https://saascend-org.github.io/dxrcyber-lead-to-cash/
- Edit the content in `build/src/` (local only, git-ignored): `data.js` holds every step, flow and decision; `app.js` renders; `style.css`; `page.html`.
- Publish: `./publish.sh` (asks for the password, inlines, encrypts with AES-256-GCM and pushes only the gate).
