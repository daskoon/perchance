# Game Design Document: "What Brings You In Today?"

---

## Overview

*"What Brings You In Today?"* is a narrative-driven, decision-based simulation game set in a big-box electronics store. The player assumes the role of a former field technician who, after losing their driving position due to traffic violations, is reassigned to a dual-role as a front-desk host and asset protection associate. The game explores the mundane and often absurd realities of retail work, from customer service to loss prevention and internal store politics.

---

## Core Gameplay Loop

1. **Clocking In & Daily Setup**
   - Arrive at work on time.
   - Receive a briefing from management.
   - Establish initial stats (Customer Patience, Self-Boredom, Manager Annoyance, Theft Loss).

2. **Customer Interactions**
   - Engage with customers via branching dialogue trees.
   - Each dialogue choice impacts key metrics (e.g., customer satisfaction, self-boredom, and manager annoyance).

3. **Asset Protection**
   - Monitor security cameras.
   - Respond to theft alerts and suspicious activities.
   - Balance intervention decisions with potential impacts on store loss and managerial response.

4. **Coworker Dynamics**
   - Interact with various coworkers:
     - **Asset Protection Partner:** A younger, energetic associate focused on theft prevention, whose perspective often contrasts with the player's more customer-service-oriented approach.
     - **Veteran Sales Staff:** Seasoned employees who offer mentorship or express skepticism.
     - **Young Sales Associates:** Enthusiastic but inexperienced staff with whom relationships can be built or strained.
   - Use dialogue choices to build relationships that influence store morale and career advancement.

5. **Store Environment & Floor Plan**
   - Navigate different areas of the store, each with its own function:
     - **Front Desk/Customer Service Area**
     - **Security Room**
     - **Break Room (with employee-only facilities such as a break room, manager offices, and a security room)**
     - **Warehouse:** Located at the very back, where inventory is stored.
   - The floor plan is designed with a clear, top-down layout, allowing for distinct sections (e.g., mobile devices, TVs, appliances) and giving a sense of scale and navigation reminiscent of a "Where's Waldo?" style map.

6. **End of Shift & Performance Review**
   - Evaluate the shift based on metrics (customer satisfaction, theft incidents, managerial feedback).
   - Outcomes affect job security, potential promotions, and relationships with coworkers and managers.
   - Multiple endings are possible depending on overall performance and the relationships built over the course of the day.

---

## Characters

### Player Character
- **Background:** Former field technician transitioning into a retail role.
- **Focus:** Primarily responsible for customer service, with asset protection duties as a secondary role.
- **Visual Style:** Rendered as a simple, minimalist bust with interchangeable facial expressions (neutral, happy, sad, worried, surprised).

### Coworkers
- **Asset Protection Partner:**
  - **Description:** A younger, enthusiastic associate with a strong focus on theft prevention.
  - **Dynamic:** Often suggests a more aggressive approach to security, creating a dynamic contrast with the player’s customer-service-centric style.
- **Sales Staff:**
  - **Veteran Sales Staff:**
    - **Description:** Older, experienced employees who provide guidance and sometimes skeptical commentary on the player’s methods.
  - **Young Sales Associates:**
    - **Description:** Employees in their 20s who are energetic and eager but sometimes lack experience, offering opportunities for bonding or rivalry through dialogue.

### Management Team
- **Sales Manager:** Oversees the sales floor and customer conversion rates.
- **Product Manager:** Manages inventory, product placement, and overall stock levels.
- **Repair Manager:** In charge of the repair department, addressing customer complaints about faulty products.
- **General Manager (GM):** The top authority, balancing overall store performance and employee relations.

---

## Mechanics & Systems

### Metrics & Variables
- **Customer Patience Bar:** Reflects the tolerance level of customers; affected by response quality and speed.
- **Self-Boredom Bar:** Indicates the player’s engagement level during repetitive tasks; can be mitigated through interactions and breaks.
- **Manager Annoyance Meter:** Increases when performance or policy expectations are not met.
- **Theft Loss Counter:** Tracks financial losses due to theft incidents, influencing managerial evaluations.

### Time & Event System
- **Shift Progression:** Time advances in discrete increments (e.g., minutes or hours).
- **Scheduled and Random Events:**
  - Planned interactions (e.g., customer greetings, coworker conversations).
  - Random events such as sudden theft alerts or unexpected rushes.
  
### Dialogue System
- Branching dialogue trees allow the player to choose responses during customer interactions, coworker conversations, and managerial briefings.
- Each dialogue choice has direct effects on the game metrics and can unlock additional narrative branches or relationship developments.

### Asset Protection Gameplay
- **Surveillance:** Monitor security camera feeds in the security room.
- **Interventions:** Decide when to intervene during potential theft events.
- **Consequences:** Choices during these events affect the Theft Loss Counter and Manager Annoyance Meter.

### Visual Presentation
- **Character Art:** Minimalist, child-like silhouettes with layered facial expressions for dynamic emotion display.
- **UI Elements:** Clean, functional menus with real-time updates of time and metric bars.
- **Floor Plan:** A detailed top-down digital illustration showing key store areas (entrance, front desk, security room, break room, warehouse) with a Where’s Waldo-esque feel of bustling activity.

---

## Visual Style & Asset Requirements

### Character Assets
- **Player Character:**
  - `player_neutral.png`
  - `player_happy.png`
  - `player_sad.png`
  - `player_worried.png`
  - `player_surprised.png`
- **Partner (Asset Protection Associate):**
  - `partner_enthusiastic.png`
  - Additional expressions as needed.
- **Sales Staff:**
  - `sales_veteran_neutral.png`
  - `sales_young_neutral.png`
- **Managers:**
  - `sales_manager_neutral.png`
  - `product_manager_neutral.png`
  - `repair_manager_neutral.png`
  - `gm_neutral.png`
- **Customer:**
  - `customer_neutral.png`
- **Scene Backgrounds:**
  - Store Entrance, Desk Area, Security Room, Break Room, Warehouse.
- **UI Elements:**
  - Time display, metric bars, game over screen, etc.

### Style Prompts (for image generation)
- **Minimalist Silhouettes:** "A very simple, blobby children's drawing-style silhouette of [character role], rendered as a minimalistic bust view with interchangeable facial expression overlays in a playful, cartoonish style."
- **Backgrounds:** "A clean, digital illustration of a [store area] with a minimalistic, modern design, clear signage, and distinct zones for customer service, security, and break areas."

---

## Development Phases

### 1. Testing Phase
- **Objective:**  
  - Implement core mechanics, dialogue trees, time progression, and asset protection systems.
  - Develop initial prototypes and conduct thorough testing.
- **Tasks:**  
  - Set up the Ren'Py project with version control.
  - Code the basic framework for shift progression, dialogue, and event triggers.
  - Create placeholder art and test expression layering.
  - Develop test cases for all core interactions (customer service, security events, coworker dialogues).
  - Document bugs and iterate until all test cases are passed.

### 2. Production Phase
- **Objective:**  
  - Expand the narrative, deepen character interactions, and refine gameplay mechanics.
  - Integrate additional art assets and polish UI elements.
- **Tasks:**  
  - Develop extended dialogue trees for customer and coworker interactions.
  - Flesh out each manager’s role and integrate them into the narrative.
  - Implement random events and additional asset protection scenarios.
  - Refine time and event pacing based on playtesting feedback.
  - Ensure integration of all visual assets with smooth transitions.

### 3. Release Phase
- **Objective:**  
  - Finalize all game elements and prepare for deployment.
  - Optimize performance and conduct final QA testing.
- **Tasks:**  
  - Complete final art, audio, and UI polish.
  - Resolve all remaining bugs and optimize code for target platforms (PC and potential Android port).
  - Finalize documentation, help files, and marketing materials.
  - Launch the game and monitor post-release feedback for patches if necessary.

---

## End Goals & Narrative Outcomes

- **Employment Stability:**  
  - Achieve a balance between customer satisfaction, effective asset protection, and positive managerial feedback.
- **Relationship Dynamics:**  
  - Build strong partnerships with the asset protection partner and navigate complex relationships with sales staff and managers.
- **Store Performance:**  
  - Prevent theft, manage customer flow, and contribute to overall store success.
- **Multiple Endings:**  
  - Outcomes vary based on player decisions, performance metrics, and relationship dynamics, leading to different career trajectories or job termination.

---

This updated document serves as the comprehensive blueprint for "What Brings You In Today?" and will evolve as development progresses. All future work should refer back to these guidelines to ensure consistency in narrative, mechanics, and visual presentation.
