---
title: "Lesson 18: Human Visual Fatigue Limits & Dynamic Presentation Velocity"
difficulty: Advanced
prerequisites:
  - "[[14-Browser-Rendering-Engines|Lesson 14: Browser Rendering Engines]]"
  - "[[15-Multithreaded-Web-Performance|Lesson 15: Multithreaded Web Performance]]"
  - "[[16-ISA-101-High-Performance-HMI|Lesson 16: ISA-101 High-Performance HMI Design]]"
  - "[[17-Situational-Awareness-Cognitive-Mirroring|Lesson 17: Situational Awareness & Cognitive Mirroring]]"
core_concepts:
  - "Information Presentation Speed (Visual Angle Velocity in deg/s)"
  - "The Tong et al. (2026) Empirical Ergonomic Study"
  - "Optimal Presentation Velocity Zone (4 deg/s to 12 deg/s)"
  - "Decision Error Escalation Threshold (> 8 deg/s) and SA Collapse Boundary (>= 16 deg/s)"
  - "Ocular Biomarkers: Saccadic Search, Blink Rate Suppression, Critical Flicker Fusion (CFF)"
  - "The Pupil Diameter Fallacy in Dynamic Visual Tracking"
  - "GPU Animation Velocity Throttling & Browser Frame Rate Clamping"
tags:
  - visual-fatigue
  - dynamic-hmi
  - presentation-velocity
  - ocular-metrics
  - blink-rate
  - human-factors
  - situational-awareness
  - high-performance-hmi
  - scada
---

# Lesson 18: Human Visual Fatigue Limits & Dynamic Presentation Velocity

In modern industrial supervisory systems, the widespread adoption of web-native rendering engines (HTML5 Canvas, WebGL, and SVG) has introduced an explosion of dynamic graphical motion. From mobile autonomous guided vehicles (AGVs) navigating factory grids ([[Guo_et_al_2022|Guo et al., 2022]]) to animated fluid streams traversing chemical piping schematics, operators are increasingly subjected to moving visual elements. However, human neuro-visual perception evolved for static surveillance punctuated by salient motion cues—not continuous multi-target pursuit. 

Grounding dynamic HMI design in empirical cognitive ergonomics ([[Tong_et_al_2026|Tong et al., 2026]]) is mandatory to prevent operator visual fatigue, ocular desiccation, and decision-making failure during critical plant operations.

---

## 1. Context & Industrial Friction: The Proliferation of Dynamic Motion in Web SCADA

In legacy distributed control systems (DCS) and hardwired mosaic mimic panels, process graphics were overwhelmingly static. Piping runs, vessel silhouettes, and pump indicators remained fixed; changes were conveyed strictly through discrete numerical updates, state-color transitions, or mechanical annunciator drop-flags. While visually austere, this static paradigm imposed minimal kinetic strain on the human oculomotor system.

The advent of modern, low-code, web-based SCADA platforms—powered by hardware-accelerated WebGL scene graphs, CSS transitions, and SVG transforms ([[13-Declarative-SVG-Synthesis|Lesson 13]], [[14-Browser-Rendering-Engines|Lesson 14]])—has democratized dynamic animation. UI designers routinely implement:
1. **Kinetic Fluid Flow Tickers:** Polygons and dashes continuously sliding along process lines to indicate fluid velocity.
2. **Rotating Turbomachinery & Impellers:** Continuously spinning SVG glyphs simulating pump, fan, or agitator rotation.
3. **Mobile Logistics & Fleet Tracking:** Real-time 2D Cartesian translations of Autonomous Guided Vehicles (AGVs) and autonomous mobile robots (AMRs) traversing warehouse and shop-floor grids ([[Guo_et_al_2022]]).
4. **Auto-Scrolling Time-Series Banners:** Real-time process historians continuously panning line charts horizontally across operator consoles.

The physical control environment and multi-display tracking contexts examined in empirical ergonomic research are illustrated in **Figure 18.1**:

![[18-modern-control-room-workstation.jpg]]
*(a) Modern Supervisory Multi-Display Workstation*

![[18-industrial-agv-fleet-warehouse.jpg]]
*(b) Industrial AGV Fleet Logistics Grid ([[Guo_et_al_2022]])*

*Figure 18.1: Physical Control Environment Context: (a) Multi-display supervisory workstation where operators track distributed facility units; (b) Autonomous Guided Vehicle (AGV) logistics facility transmitting high-frequency positioning telemetry ([[Guo_et_al_2022]]).*

### The Engineering Friction: The Literal Physics Trap
When web developers integrate real-time physical telemetry—such as AGV coordinates streamed over MQTT ([[Guo_et_al_2022]]) or fluid velocity from Sparkplug B transmitters—they frequently fall into the **Literal Physics Trap**: *attempting to scale screen animation speed directly proportional to actual physical velocity*.

As empirical human-factors research demonstrates, accurately depicting the physical speed of a moving fluid or vehicle directly onto a screen display induces severe cognitive failure ([[Tong_et_al_2026]]). When visual elements translate too quickly across an operator's visual field, the oculomotor tracking system shifts from exploratory saccades into continuous, strained [[../Glossary#Smooth Pursuit Blink Suppression|smooth pursuit]]. Under sustained pursuit, attentional demand skyrockets and rapidly depletes the cognitive reserve needed to detect abnormal alarms. Concurrently, spontaneous blinking is reflexively suppressed, causing corneal drying and ocular asthenopia. Ultimately, target search accuracy collapses, precipitating erroneous control inputs and severe situational awareness failure.

---

## 2. Biomechanical Foundations: Retinal Sweep & [[../Glossary#Visual Angle Velocity ($\omega$)|Visual Angle Velocity]] Mechanics

In software engineering, UI motion is almost universally specified in display-centric units: **pixels per second (px/s)**. In human biophysics, however, *pixels per second is a completely ungrounded and meaningless metric*.

### The Resolution/Distance Confounding Trap
Consider an animation configured to move at $v_{\text{screen}} = 200\text{ px/s}$:
1. **Desktop Operator Console (24-inch 1080p Display):**
   - Pixel pitch: $p \approx 0.276\text{ mm/px}$.
   - Physical translation: $200 \times 0.276 = 55.2\text{ mm/s}$.
   - Viewing distance: $D = 650\text{ mm}$.
   - Angular velocity: $\omega \approx 4.86^\circ/\text{s}$ (well within the optimal ergonomic window).
2. **Central Video Wall / Large Overview Display (85-inch 4K Display):**
   - Pixel pitch: $p \approx 0.489\text{ mm/px}$.
   - Physical translation: $200 \times 0.489 = 97.8\text{ mm/s}$.
   - Viewing distance: $D = 2200\text{ mm}$.
   - Angular velocity: $\omega \approx 2.55^\circ/\text{s}$ (sluggish, causing delayed situational awareness).
3. **Mobile Rugged Tablet (10.1-inch 1920x1200 Display):**
   - Pixel pitch: $p \approx 0.113\text{ mm/px}$.
   - If an engineer sets a fast sweep of $800\text{ px/s} = 90.4\text{ mm/s}$.
   - Viewing distance: $D = 320\text{ mm}$.
   - Angular velocity: $\omega \approx 16.18^\circ/\text{s}$ (**exceeds safe limits; situational awareness collapses**).

The biological human eye reacts strictly to the rate at which an image traverses the retina: **degrees of visual angle per second ($^\circ/\text{s}$)**.

### Mathematical Derivation of Retinal Angular Velocity
Let $S$ represent the physical displacement distance of a graphical symbol across a flat display screen (in millimeters), and let $D$ represent the orthogonal viewing distance from the operator's eye to the display surface (in millimeters).

The subtended visual angle $\theta$ (in degrees) is derived trigonometrically:

$$\theta = 2 \cdot \arctan\left(\frac{S}{2D}\right) \cdot \frac{180}{\pi}$$

Differentiating with respect to time $t$ yields the instantaneous angular velocity $\omega$ (in $^\circ/\text{s}$):

$$\omega = \frac{d\theta}{dt} = \frac{360}{\pi} \cdot \left[ \frac{2D}{4D^2 + S^2} \right] \cdot \frac{dS}{dt}$$

For standard supervisory tasks where displacement $S$ over a small discrete frame interval $\Delta t$ is small relative to viewing distance ($S \ll D$), this simplifies to:

$$\omega \approx \frac{180}{\pi D} \cdot \frac{dS}{dt} = \frac{180}{\pi D} \cdot \left( v_{\text{px}} \cdot p_{\text{pitch}} \right)$$

where $v_{\text{px}}$ is the screen velocity in $\text{px/s}$ and $p_{\text{pitch}}$ is the display's physical pixel pitch in $\text{mm/px}$.

### Retinal Acuity Cones & Visual Field Organization
Human vision is not uniform across the visual field:
- **Foveal Vision ($1^\circ\text{–}2^\circ$ Cone):** Centered on the fovea centralis, packed with high-density cone photoreceptors. This is the only zone capable of resolving fine alphanumeric text, small sensor readings, and subtle alarm priority digits.
- **Parafoveal Vision ($2^\circ\text{–}5^\circ$ Cone):** Lower spatial acuity; capable of recognizing analog gauge levels, moving pointer directions, and broad symbol geometry without direct fixation.
- **Near-Peripheral Field ($5^\circ\text{–}30^\circ$ Cone):** Extremely low spatial resolution, but optimized for transient flicker, high-contrast flashing, and motion detection. Motion in this zone triggers involuntary ocular reflexes.
- **Far-Peripheral Field ($>30^\circ$):** Detects gross movement. High-speed graphical movement here draws attention away from central supervisory tasks, inducing severe distraction.

The trigonometric relationship between screen displacement, viewing distance, and retinal field cones is diagrammed in **Figure 18.2**:

![[18-visual-angle-geometry-ergonomics.svg]]

*Figure 18.2: Biomechanical Optical Geometry: Retinal visual angle calculation ($\theta = 2 \arctan(S/2D)$) and optical field cones (foveal $1^\circ\text{–}2^\circ$, parafoveal $2^\circ\text{–}5^\circ$, near-peripheral $5^\circ\text{–}30^\circ$, far-peripheral $>30^\circ$). The right panel illustrates the Resolution/Distance Confounding Trap, proving why raw pixels-per-second is invalid across industrial form factors ([[Tong_et_al_2026]]).*

---

## 3. Empirical Grounding: The Tong et al. (2026) Ergonomic Findings

To establish scientifically rigorous presentation boundaries for industrial control systems, **[[Tong_et_al_2026|Tong et al. (2026)]]** conducted a landmark human-factors study evaluating operator visual search performance, cognitive workload, situational awareness, and eye-tracking biomarkers across eight discrete angular velocities:

$$v \in \{1, 2, 4, 8, 12, 16, 24, 32\} \quad (^\circ/\text{s})$$

### The Three Empirical Velocity Zones
The empirical findings demarcate three distinct operational regimes:

| Velocity Zone | Angular Velocity ($\omega$) | Cognitive & Physiological Impact | Example design response |
| :--- | :--- | :--- | :--- |
| **Sub-Optimal Slow Zone** | $\omega < 4^\circ/\text{s}$ | Sub-optimal visual scanning; sluggish updates; high saccadic latency between slowly drifting targets; operator boredom and delayed anomaly awareness. | **Acceleration / Stepping:** Boost to $4^\circ/\text{s}$ or replace with discrete step increments. |
| **Optimal Ergonomic Window** | **$4^\circ/\text{s} \le \omega \le 12^\circ/\text{s}$** | **Peak performance:** Target visual search accuracy exceeds $95\%$; balanced SART attentional demand and supply; normal spontaneous blink rate ($15\text{–}22\text{ blinks/min}$); zero visual fatigue accumulation. | **Mandatory Standard:** All dynamic flow synoptics and AGV tracking vectors strictly bounded within this window. |
| **Hazard & Collapse Zone** | $\omega \ge 16^\circ/\text{s}$ | **Severe failure:** Target search accuracy collapses below $65\%$ (dropping to $54.2\%$ at $32^\circ/\text{s}$); SART attentional demand exceeds supply; spontaneous blink rate plummets; [[../Glossary#Critical Flicker Fusion (CFF)|Critical Flicker Fusion (CFF)]] drops precipitously. | **Hard Architectural Stop:** High velocities strictly clamped or converted to static rate indicators / strobe badges. |

### The Critical Discovery: The [[../Glossary#Decision Reaction Fallacy|Decision Reaction Fallacy]]
A pivotal insight from [[Tong_et_al_2026|Tong et al. (2026)]] concerns the precise nature of operator failure under speed stress. A post-hoc decomposition of error types revealed that:
$$\text{Speed increases affect operators' \textbf{incorrect decision reactions}, NOT their omissions! } (p < 0.001)$$

At high presentation velocities ($\ge 16^\circ/\text{s}$):
- **Omission Rate (Missed Targets):** Remains statistically flat. Operators still perceive that *something* is moving across the screen; their peripheral visual motion sensors register the event.
- **Incorrect Action Rate (Erroneous Decisions):** Escalates dramatically. When forced to process high-speed dynamic elements, operators suffer cognitive executive breakdown. They misidentify process parameters, confuse valve states, and trigger erroneous manual override actions.

### SART Attentional Demand vs. Supply Crossover
Using the **[[../Glossary#Situation Awareness Rating Technique (SART)|Situation Awareness Rating Technique (SART)]]**, [[Tong_et_al_2026|Tong et al.]] tracked three core cognitive dimensions:
1. **Attentional Demand ($D$):** The cognitive effort required to perceive and track moving elements. Climbs steeply once presentation speed exceeds $8^\circ/\text{s}$ (from a baseline score of $22$ up to $84$ at $32^\circ/\text{s}$).
2. **Attentional Supply ($S$):** The spare cognitive capacity available to process alarms and context. Plummets from $86$ down to $24$ as velocity escalates.
3. **Understanding ($U$):** The operator's mental model of the underlying process schematic. **Remains statistically unchanged ($p > 0.05$) across all velocities.**

This proves conclusively that operational breakdown at high velocities is **purely a failure of attentional bandwidth and oculomotor mechanics**, not a deficit in operator plant training or schematic understanding! At $\omega \approx 14^\circ\text{–}16^\circ/\text{s}$, demand crosses supply ($D > S$), triggering immediate loss of situational awareness.

The empirical response curves and SART attentional dynamics measured across these velocity zones are plotted in **Figure 18.3**:

![[18-tong-presentation-velocity-zones.svg]]

*Figure 18.3: Empirical Response Curves from Tong et al. (2026): (Left) Target search accuracy vs. decision error rate across 8 velocity treatments, highlighting the $8^\circ/\text{s}$ inversion threshold ($p < 0.001$); (Right) Situation Awareness Rating Technique (SART) attentional dynamics showing the crossover of attentional exhaustion ($\omega \approx 14^\circ/\text{s}$) where demand surpasses available supply.*

---

## 4. Ocular Biomarkers & The [[../Glossary#Dynamic Pupil Diameter Fallacy|Dynamic Pupil Diameter Fallacy]]

Eye-tracking technology is increasingly integrated into industrial control rooms to monitor operator alertness and mental fatigue. However, analyzing ocular metrics in dynamic supervisory environments requires understanding human oculomotor mechanics.

### Saccades vs. Smooth Pursuit Eye Tracking
The human eye employs two fundamentally distinct visual tracking modes:
- **Saccades:** Ballistic, high-velocity jumps ($200^\circ\text{–}900^\circ/\text{s}$) between fixation targets. During a saccade, visual perception is suppressed (saccadic masking), and the brain executes spontaneous blinking without target loss.
- **Smooth Pursuit:** Continuous, slow tracking movements ($0^\circ\text{–}30^\circ/\text{s}$) where the eye matches the velocity of a moving object to maintain its image on the fovea centralis.

### Spontaneous Eye Blink Rate Suppression
When graphical presentation speed exceeds $16^\circ/\text{s}$, the operator's oculomotor system is forced into continuous, uninterrupted smooth pursuit. 

During smooth pursuit, the brain unconsciously **inhibits the spontaneous blink reflex** ($F(7, 133) = 3.749, p < 0.05$):
- A spontaneous eyelid closure lasts $100\text{–}150\text{ ms}$.
- At an angular speed of $24^\circ/\text{s}$, a $150\text{ ms}$ blink would cause the target to traverse $3.6^\circ$ of visual angle while unseen, causing the fovea to completely lose target lock.
- To prevent target loss, the nervous system suppresses blinking, reducing spontaneous blink frequency from a healthy $15\text{–}22\text{ blinks/min}$ down to less than $4\text{–}6\text{ blinks/min}$ ([[Tong_et_al_2026]]).

**Physiological Consequence:** Suppressed blinking exceeds the **Tear Film Breakup Time (TBUT)** ($>10\text{ s}$ unblinked). The precorneal tear film evaporates, exposing corneal nerve endings. Operators experience ocular burning, asthenopia, headache, and severe visual fatigue, directly degrading sustained vigilance during long 12-hour shifts.

### Critical Flicker Fusion (CFF) Degradation
**Critical Flicker Fusion** is the temporal frequency (in Hz) at which an intermittent light flash ceases to be perceived as flickering and appears as a continuous, steady beam. CFF serves as an objective, clinical metric of central nervous system retinocortical fatigue.
- In healthy, alert operators, baseline CFF ranges between $42\text{–}46\text{ Hz}$.
- Under optimal presentation speeds ($4^\circ\text{–}8^\circ/\text{s}$), CFF remains stable over hours of continuous monitoring.
- Under high presentation speeds ($>16^\circ/\text{s}$), CFF drops precipitously by $>5\text{–}8\text{ Hz}$ within 30 minutes, indicating profound neuro-visual exhaustion and sluggish synaptic processing in the visual cortex ([[Tong_et_al_2026]]).

### The Dynamic Pupil Diameter Fallacy
In static cognitive psychology tasks, **pupil diameter** is widely celebrated as a reliable index of cognitive workload and fatigue:
- As mental fatigue accumulates, sympathetic tone decreases and parasympathetic tone increases, causing **pupillary constriction (miosis)**.
- Many legacy AI-driven monitoring proposals recommend tracking operator pupil diameter to trigger adaptive interface simplification.

However, **[[Tong_et_al_2026|Tong et al. (2026)]] established conclusively that average pupil diameter is an invalid, ungrounded metric for dynamic supervisory tasks.**

#### The Physiological Antagonistic Push-Pull Mechanism:
The human iris is governed by two antagonistic autonomic nervous pathways acting simultaneously during dynamic visual monitoring:
1. **Pathway A: Parasympathetic Fatigue Constriction (Miosis):**
   - High cognitive workload and sustained visual fatigue stimulate the Edinger-Westphal nucleus via the parasympathetic system, activating the circular *sphincter pupillae* muscle.
   - **Vector Effect:** Constriction ($-\Delta r$).
2. **Pathway B: Sympathetic Motion Tracking Dilation (Mydriasis):**
   - Actively tracking fast-moving targets across a screen triggers autonomic sympathetic arousal and mental effort, stimulating the radial *dilator pupillae* muscle via the superior cervical ganglion.
   - **Vector Effect:** Dilation ($+\Delta r$).

Because these two physiological mechanisms act in direct, equal opposition during dynamic tracking tasks:

$$\Delta r_{\text{net}} = (-\Delta r_{\text{fatigue}}) + (+\Delta r_{\text{tracking}}) \approx 0$$

The net pupil diameter shows **zero statistically significant variance across all eight presentation velocities ($p > 0.05$)** ([[Tong_et_al_2026]]). 

> [!CAUTION] System Design Rule: Reject Pupil-Based Adaptive SCADA
> Industrial HMI software must NEVER use pupil diameter measurements to detect operator fatigue or trigger dynamic interface adaptations in moving displays. Any fatigue-monitoring algorithm relying on pupil size in dynamic environments is mathematically and biologically ungrounded.

The physiological mechanisms of blink suppression, CFF decay, and the antagonistic push-pull pupillary model are illustrated in **Figure 18.4**:

![[18-ocular-biomarkers-pupil-fallacy.svg]]

*Figure 18.4: Physiological Breakdown & The Dynamic Pupil Fallacy: (Top) Progressive stages of smooth pursuit blink reflex inhibition ($F(7,133) = 3.749, p < 0.05$) leading to corneal desiccation; (Bottom Left) CFF decay over time across velocity treatments; (Bottom Right) The Push-Pull Antagonistic Model of Pupillary Cancellation, proving why average pupil diameter is an ungrounded metric in dynamic displays ([[Tong_et_al_2026]]).*

---

## 5. Applied Software Architecture: The Web SCADA Motion Governor Pipeline

To eliminate the Literal Physics Trap and respect the empirical boundaries of [[Tong_et_al_2026|Tong et al. (2026)]], a web HMI can implement a **Retinal Motion Governor Pipeline**.

### Architectural Invariant: [[../Glossary#Dynamic Presentation Velocity Invariant|The Retinal Velocity Governor Rule]]
No dynamic element rendered within a synoptic display should traverse the operator's visual field at an angular velocity exceeding **$12^\circ/\text{s}$**. Any raw telemetry speed resulting in an angular velocity $\ge 16^\circ/\text{s}$ can be clamped or converted to a discrete, non-pursuit visual representation (ANSI/ISA-101.01).

### The 4-Stage Motion Governor Execution Flow
1. **Telemetry Normalization:** Ingests raw physical velocities: AGV Cartesian coordinates $(x, y, v_{\text{phys}})$ via MQTT 4-level topics (`01/stm32/data/agv_pose`, per [[Guo_et_al_2022]]), or volumetric pipeline flow rates ($Q_{\text{fluid}}$) via Sparkplug B.
2. **Viewport Geometry Profiling:** Queries client display properties (`window.devicePixelRatio`, screen resolution, and physical dimensions) and reads calibrated operator viewing distance $D$ ($650\text{ mm}$ for desktop consoles, $2200\text{ mm}$ for LOD video walls, or dynamic depth sensor inputs).
3. **Retinal Angular Velocity Governor:** Computes unconstrained angular velocity $\omega_{\text{raw}} = \frac{180}{\pi D} \cdot v_{\text{phys\_screen}}$ and applies the selected motion policy:
   - If $\omega_{\text{raw}} < 4^\circ/\text{s}$: Applies subtle discrete pulse stepping to eliminate sluggish scanning.
   - If $4^\circ/\text{s} \le \omega_{\text{raw}} \le 12^\circ/\text{s}$: Linear pass-through (Optimal Ergonomic Window).
   - If $12^\circ/\text{s} < \omega_{\text{raw}} < 16^\circ/\text{s}$: Logarithmic dampening curve smoothly capping speed at $12^\circ/\text{s}$.
   - If $\omega_{\text{raw}} \ge 16^\circ/\text{s}$: **Hard Velocity Clamp** + Fallback Mode: transitions from continuous smooth-pursuit animation to a static chevron or discrete 1 Hz strobe rate indicator per ANSI/ISA-101.01.
4. **Decoupled GPU Rendering:** Dispatches clamped animation parameters to an `OffscreenCanvas` Web Worker ([[15-Multithreaded-Web-Performance|Lesson 15]]) and updates hardware-accelerated CSS GPU matrix transforms (`transform: translate3d(x, y, 0)`), guaranteeing zero main-thread layout thrashing and rock-solid 60 FPS performance.

The multi-stage architecture and Web Worker execution pipeline of the motion governor are diagrammed in **Figure 18.5**:

![[18-web-scada-motion-governor-pipeline.svg]]

*Figure 18.5: Web SCADA Motion Governor Pipeline: Ingesting MQTT 4-level topics ([[Guo_et_al_2022]]) and Sparkplug B telemetry, profiling client viewport geometry ($D$ and $p$), clamping retinal angular velocity ($4^\circ/\text{s} \le \omega \le 12^\circ/\text{s}$), and offloading to an OffscreenCanvas GPU worker thread.*

### Strict TypeScript Implementation: `RetinalMotionGovernor.ts`

```typescript
/**
 * RetinalMotionGovernor.ts
 * Enforces empirical presentation velocity boundaries (Tong et al., 2026).
 * Strictly complies with ANSI/ISA-101.01 High-Performance HMI standards.
 */

export interface ViewportProfile {
  /** Viewing distance from operator eye to screen in millimeters (e.g., 650 mm) */
  readonly viewingDistanceMm: number;
  /** Physical screen pixel pitch in millimeters per pixel (e.g., 0.276 mm/px for 24" 1080p) */
  readonly pixelPitchMm: number;
}

export interface ClampedMotionResult {
  /** Governed angular velocity in degrees of visual angle per second */
  readonly omegaDegPerSec: number;
  /** Resulting screen translation velocity in pixels per second for CSS translate3d */
  readonly renderPxPerSec: number;
  /** True if speed exceeded danger boundary (>=16 deg/s), requiring discrete strobe mode */
  readonly fallbackStrobeActive: boolean;
}

export class RetinalMotionGovernor {
  // Empirical boundaries from Tong et al. (2026)
  public static readonly MIN_SAFE_OMEGA = 4.0;   // 4°/s: Below this causes sluggish scanning
  public static readonly MAX_SAFE_OMEGA = 12.0;  // 12°/s: Upper bound of optimal ergonomic zone
  public static readonly DANGER_CEILING = 16.0;  // 16°/s: Hard stop; triggers blink suppression & SA collapse

  /**
   * Translates raw physical velocity into a retinally-governed screen speed.
   * @param physicalSpeedMmPerSec Raw real-world or virtual speed in mm/s on display surface
   * @param profile Viewport and optical viewing distance profile
   */
  public static computeClampedVelocity(
    physicalSpeedMmPerSec: number,
    profile: ViewportProfile
  ): ClampedMotionResult {
    const D = profile.viewingDistanceMm;
    const p = profile.pixelPitchMm;

    // Small-angle derivative: omega = (180 / PI) * (v_mm / D)
    const rawOmega = (180.0 / Math.PI) * (physicalSpeedMmPerSec / D);

    // Hazard Boundary Check: Tong et al. proved >=16 deg/s induces cognitive breakdown
    if (rawOmega >= this.DANGER_CEILING) {
      // Return hard-clamped maximum safe speed and signal fallback to static/strobe mode
      const clampedPx = (this.MAX_SAFE_OMEGA * (Math.PI / 180.0) * D) / p;
      return {
        omegaDegPerSec: this.MAX_SAFE_OMEGA,
        renderPxPerSec: clampedPx,
        fallbackStrobeActive: true,
      };
    }

    // Optimal Zone Clamping: 4°/s <= omega <= 12°/s
    const clampedOmega = Math.max(this.MIN_SAFE_OMEGA, Math.min(this.MAX_SAFE_OMEGA, rawOmega));
    const renderPx = (clampedOmega * (Math.PI / 180.0) * D) / p;

    return {
      omegaDegPerSec: clampedOmega,
      renderPxPerSec: renderPx,
      fallbackStrobeActive: false,
    };
  }
}
```

---

## 6. Active-Recall Assessments

> [!FAQ]- Why must dynamic animation speeds on an industrial SCADA screen be constrained in degrees of visual angle per second (°/s) rather than measured in screen pixels per second (px/s)?
> Measuring speed in pixels per second is device-dependent and physiologically ungrounded. A symbol moving at $200\text{ px/s}$ on a $24\text{"}$ 1080p monitor viewed from $650\text{ mm}$ produces an angular velocity of $\approx 4.86^\circ/\text{s}$ (within the optimal ergonomic zone). However, moving that same symbol at $200\text{ px/s}$ on an $85\text{"}$ 4K video wall viewed from $2200\text{ mm}$ yields $\approx 2.55^\circ/\text{s}$ (sluggish, sub-optimal), while moving it at $800\text{ px/s}$ on a high-DPI rugged tablet viewed from $320\text{ mm}$ produces $\approx 16.18^\circ/\text{s}$ (severe situational awareness collapse). Visual angle velocity ($\omega = \frac{d\theta}{dt}$ in $^\circ/\text{s}$) normalizes screen resolution and viewing distance to reflect the actual biological rate of eye motion required by the human retina ([[Tong_et_al_2026|Tong et al., 2026]]).

> [!FAQ]- What is the "Decision Reaction Fallacy" discovered by Tong et al. (2026), and why does presentation velocity above 8°/s impair decision accuracy rather than target perception?
> When presentation speeds exceed $8^\circ/\text{s}$, post-hoc empirical analysis demonstrates that the error rate escalation is driven almost entirely by an increase in **incorrect operational decisions**, while non-response target omission rates remain statistically flat ($p < 0.001$). Operators still perceive that an element is moving across their visual field, but the cognitive executive processing bandwidth required to interpret symbol semantics, check secondary context, and evaluate trade-offs breaks down under speed stress. This induces hasty, erroneous control actions rather than missed signals ([[Tong_et_al_2026|Tong et al., 2026]]).

> [!FAQ]- Describe the biomechanical mechanism by which smooth pursuit tracking above 16°/s inhibits spontaneous blinking, and explain the resulting physiological damage.
> Tracking moving targets at angular velocities $\ge 16^\circ/\text{s}$ forces the oculomotor system into continuous, uninterrupted smooth pursuit. Because an eyelid closure takes $100\text{–}150\text{ ms}$, blinking during fast smooth pursuit causes the target to jump several degrees across the retina while unseen, causing the fovea to lose target lock. To maintain visual lock, the central nervous system reflexively suppresses the spontaneous blink reflex ($F(7, 133) = 3.749, p < 0.05$), dropping blink rates from $15\text{–}22$ blinks/min down to $< 4\text{–}6$ blinks/min. This exceeds the Tear Film Breakup Time (TBUT), leading to rapid precorneal tear evaporation, corneal epithelial desiccation, eye burning (asthenopia), and severe visual fatigue that impairs sustained vigilance ([[Tong_et_al_2026|Tong et al., 2026]]).

> [!FAQ]- Why is pupil diameter an invalid and ungrounded metric for detecting operator fatigue in dynamic supervisory displays, despite being effective in static tasks?
> In static cognitive tasks, visual and mental fatigue causes pupillary constriction (miosis) via parasympathetic activation. However, actively tracking rapid dynamic motion stimulates sympathetic autonomic arousal, which causes pupillary dilation (mydriasis). In dynamic supervisory displays, these two opposing autonomic nervous pathways operate simultaneously: the parasympathetic constriction induced by fatigue is cancelled out by the sympathetic dilation induced by motion tracking arousal. Because the two forces act in direct push-pull opposition, net pupil diameter shows zero statistically significant change across presentation velocities ($p > 0.05$), making pupil size an ungrounded metric for dynamic HMI evaluation ([[Tong_et_al_2026|Tong et al., 2026]]).
