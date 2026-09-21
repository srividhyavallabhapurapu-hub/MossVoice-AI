# Product Requirements Document (PRD): AI Voice Marketing & CRM Assistant

## 1. Executive Summary
The **AI Voice Marketing & CRM Assistant** is a real-time, voice-first application designed to empower sales and marketing professionals with hands-free, instant access to CRM data. By leveraging **LiveKit** for low-latency audio streaming and **Moss** for sub-10ms semantic context retrieval, the system allows users to query lead information, check campaign statuses, and receive AI-driven follow-up suggestions through natural conversation.

## 2. Problem Statement
Sales and marketing teams, particularly field workers and account executives, often struggle to access critical CRM data while on the move or during multitasking. Navigating complex CRM interfaces (like Salesforce) on mobile devices is time-consuming and distracting. There is a need for a "heads-up" conversational interface that provides instant, context-aware information without the friction of manual searching.

## 3. Goals & Objectives
*   **Real-Time Responsiveness:** Achieve near-instant voice interactions using low-latency protocols.
*   **Seamless CRM Integration:** Provide a unified voice interface for Salesforce data.
*   **Contextual Intelligence:** Use semantic retrieval to ensure the AI understands the specific business context of every query.
*   **Efficiency:** Reduce the time taken to retrieve lead and campaign details by at least 70% compared to manual CRM navigation.
*   **Hackathon Success:** Deliver a functional MVP that demonstrates the full "Voice -> Moss -> Salesforce -> Voice" loop.

## 4. Target Users / Stakeholders
*   **Field Sales Representatives:** Need quick briefings on leads before meetings.
*   **Marketing Managers:** Need real-time updates on campaign performance and lead quality.
*   **Customer Support/Success:** Need instant history on customers during high-stakes calls.
*   **System Administrators:** Responsible for maintaining CRM data integrity and security.

## 5. Functional Requirements
### 5.1 Voice Interaction
*   **Real-Time Streaming:** The system must support full-duplex voice communication using LiveKit.
*   **Speech-to-Text (STT):** Convert user voice input into text with high accuracy and low latency.
*   **Text-to-Speech (TTS):** Generate natural-sounding voice responses for the user.

### 5.2 CRM & Data Operations (Salesforce)
*   **Lead Lookup:** Retrieve lead details (name, status, contact info) via voice command.
*   **Customer Info Lookup:** Access historical data and notes for existing contacts.
*   **Campaign Information:** Query active marketing campaigns and their associated metrics.
*   **Lead Prioritization:** AI-driven suggestions on which leads to contact first based on CRM data.
*   **Follow-up Suggestions:** Generate recommended next steps or message drafts after a conversation.

### 5.3 Knowledge Retrieval (Moss)
*   **Sub-10ms Retrieval:** Use Moss to store and retrieve semantic context (e.g., product documentation, sales scripts, or specific CRM context) to ground the AI's responses.
*   **Contextual Awareness:** Ensure the AI agent uses retrieved context to provide accurate, non-hallucinated answers.

## 6. Non-Functional Requirements
*   **Latency:** End-to-end voice-to-voice latency should ideally be under 1.5 seconds, with Moss retrieval taking <10ms.
*   **Scalability:** The backend (FastAPI) and voice server (LiveKit) must support multiple concurrent sessions.
*   **Reliability:** Graceful handling of network interruptions or CRM API timeouts.
*   **Security:** All voice data and CRM credentials must be encrypted in transit and at rest.

## 7. System Architecture Overview
The system follows a modern, event-driven architecture:
1.  **Frontend (Next.js):** Provides the user interface for authentication, session management, and visual feedback of the voice interaction.
2.  **Voice Layer (LiveKit):** Handles the WebRTC connection, audio transport, and room management.
3.  **Orchestration Layer (FastAPI):** The central hub that manages the logic between the STT/TTS engines, the LLM, Moss, and Salesforce.
4.  **Retrieval Layer (Moss):** Acts as the high-speed semantic memory for the agent.
5.  **Data Layer (Salesforce):** The source of truth for all customer and marketing data.

## 8. Tech Stack
*   **Frontend:** Next.js, Tailwind CSS, Lucide React (Icons).
*   **Backend:** Python 3.10+, FastAPI.
*   **Voice/WebRTC:** LiveKit SDK & Cloud/Self-hosted server.
*   **Semantic Retrieval:** Moss (Mandatory for low-latency context).
*   **CRM:** Salesforce (REST API / Bulk API).
*   **AI/LLM:** OpenAI (GPT-4o) or Anthropic (Claude 3.5 Sonnet) for reasoning; Whisper (STT) and ElevenLabs or Cartesia (TTS).
*   **Database (Metadata):** PostgreSQL or Redis (for session state).

## 9. Data Requirements
*   **CRM Schema:** Mapping of Salesforce objects (Leads, Contacts, Accounts, Campaigns) to the AI's internal data model.
*   **Vector Embeddings:** CRM data and marketing collateral must be indexed in Moss to enable semantic search.
*   **Data Flow:** 
    *   User speaks -> LiveKit -> FastAPI -> STT -> Text.
    *   Text -> Moss (Search for context) -> LLM (Process with Salesforce data) -> Response.
    *   Response -> TTS -> LiveKit -> User hears audio.

## 10. API Specifications
*   **POST `/api/voice/token`:** Generates a LiveKit access token for the frontend client.
*   **GET `/api/crm/leads/{id}`:** Fetches specific lead data from Salesforce.
*   **POST `/api/agent/interact`:** (Internal) Handles the logic of combining Moss context with LLM reasoning.
*   **Salesforce Webhooks:** (Optional) To update Moss index when CRM data changes.

## 11. Security Requirements
*   **Authentication:** NextAuth.js or similar for user login; OAuth 2.0 for Salesforce integration.
*   **Authorization:** Role-based access control (RBAC) to ensure users only see CRM data they are permitted to access.
*   **Privacy:** Ensure voice recordings are not stored longer than necessary for processing (GDPR/CCPA compliance).

## 12. Deployment & Infrastructure
*   **Containerization:** Docker for FastAPI and Next.js services.
*   **Cloud Provider:** AWS, GCP, or Vercel (Frontend) + Fly.io/Railway (Backend).
*   **CI/CD:** GitHub Actions for automated testing and deployment.
*   **Monitoring:** Sentry for error tracking; Prometheus/Grafana for LiveKit performance metrics.

## 13. Success Metrics
*   **Response Latency:** Average time from user finishing speech to AI starting speech.
*   **Retrieval Accuracy:** Percentage of queries where Moss provided relevant context.
*   **User Retention:** Frequency of use by sales team members during the pilot phase.
*   **Task Completion:** Percentage of successful lead lookups vs. failed attempts.

## 14. Timeline & Milestones (Hackathon Schedule)
*   **Phase 1 (Setup):** Initialize Next.js, FastAPI, and LiveKit connection.
*   **Phase 2 (Integration):** Connect Salesforce API and implement basic lead lookup.
*   **Phase 3 (Intelligence):** Integrate Moss for semantic retrieval and context grounding.
*   **Phase 4 (Refinement):** Optimize TTS/STT latency and polish the UI/UX.
*   **Phase 5 (Demo):** Final testing and presentation prep.

## 15. Open Questions & Risks
*   **Salesforce API Limits:** How to handle rate limiting during high-volume usage? (Mitigation: Caching/Moss).
*   **Ambient Noise:** How well will the STT perform in noisy field environments? (Mitigation: LiveKit noise cancellation).
*   **Moss Sync:** How frequently should CRM data be re-indexed into Moss to ensure "real-time" accuracy? (Mitigation: Event-driven updates).