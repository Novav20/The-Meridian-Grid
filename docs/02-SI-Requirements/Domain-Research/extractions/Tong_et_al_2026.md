---
paper_id: "Tong_et_al_2026"
query_id: "Q03"
title: "The dual effects of information presentation speed on operator performance in dynamic tasks: a study in supervisory control and data acquisition interfaces"
authors: "Tong M.; Man S.S.; Liu Y.; Bao L."
year: 2026
doi: "10.1080/00140139.2026.2686854"
keywords: ["Dynamic visual search", "pupil diameter", "situational awareness", "user interface design", "visual fatigue"]
source_pdf: "The dual effects of information presentation speed on operator performance in dynamic tasks: a study in supervisory control and data acquisition interfaces.pdf"
extraction_date: "2026-09-20"
stage2_status: "Included_Stage2"
---

### 1. Ubiquitous Language

- **Term**: Information Presentation Speed
- **Definition**: The movement velocity (measured in degrees of visual angle per second, °/s) of dynamic visual elements and graphics across a supervisory control and data acquisition interface display.
> **Evidence**: "this study examined how information presentation speed affects operator performance, subjective perception, situational awareness, and eye-tracking metrics." (p. 1)

- **Term**: Situation Awareness Rating Technique (SART)
- **Definition**: A subjective self-assessment rating scale that evaluates an operator's situational awareness across attentional demand, attentional supply, and understanding dimensions.
> **Evidence**: "additionally, participants needed to self-assess their level of situational awareness on a scale from 0 to 100, using the situation awareness Rating technique (saRt) proposed by taylor (taylor 2011)" (p. 3)

- **Term**: Blink Rate
- **Definition**: An ocular metric calculating the number of eye blinks per minute to assess operator visual fatigue and attentional strain during dynamic visual monitoring.
> **Evidence**: "Blink rate was extracted from the eye-tracking data and calculated as the number of blinks per minute during each experimental condition. Blink rate was used as an indicator of ocular activity and potential visual fatigue." (p. 4)

- **Term**: Critical Flicker Fusion (CFF)
- **Definition**: A physiological threshold measuring the temporal resolution of the visual system that decreases as visual fatigue accumulates during display tasks.
> **Evidence**: "During the experiment, the critical flicker fusion (cFF) values were also monitored to prevent the accumulation of visual fatigue, as cFF reflects the temporal resolution of the visual system and decreases as visual fatigue increases" (p. 3)

### 2. Domain Rules and Invariants

- **Rule**: Maximum Speed Threshold for Decision-Making Error Suppression
- **Mechanism**: Dynamic presentation speeds exceeding 8°/s significantly increase the probability of incorrect operational decisions without affecting non-response omission rates, demonstrating that higher speeds specifically disrupt decision-making logic rather than signal perception.
> **Evidence**: "a post-hoc analysis of the incorrect responses indicated that when the speed exceeds 8 degrees/s, the probability of incorrect responses consistently increased (p < 0.001). these findings suggested that speed changes affect the overall accuracy rate by influencing operators’ incorrect reactions rather than their omissions." (p. 6)

- **Rule**: Upper Operational Bound for Situational Awareness Preservation
- **Mechanism**: Information presentation speeds of 16°/s and above trigger a significant decline in overall operator situational awareness by continuously escalating attentional demand and diminishing remaining attentional supply.
> **Evidence**: "situational awareness levels were significantly lower at speeds of 16 degrees/s (M = 86.4, sD = 15.11), 24 degrees/s (M = 70.4, sD = 13.88), and 32 degrees/s (M = 54.2, sD = 8.97), compared to speeds lower than 16 degrees/s." (p. 7)

- **Rule**: Pupil Diameter Unreliability Invariant in Dynamic Tracking Tasks
- **Mechanism**: Pupil diameter cannot serve as a valid index of visual fatigue during dynamic visual monitoring because stimulus-tracking pupillary dilation and visual search saccades counterbalance fatigue-induced pupillary constriction.
> **Evidence**: "consequently, the study suggests that pupil diameter is an unreliable measure of eye fatigue in tasks involving dynamic visual monitoring." (p. 9)

### 3. Architectural Constraints and Patterns

- **Constraint/Pattern**: Optimal Speed Window Constraint for Dynamic SCADA Symbols
- **Implication**: HMI graphic engines must constrain dynamic visual element velocities to a range of 4–12°/s (and strictly under 16°/s) to ensure optimal operator task accuracy, maintain situational awareness, and avoid visual fatigue.
> **Evidence**: "taken together, the findings across task performance, subjective evaluation, situational awareness, and eye-tracking metrics suggest that, for dynamic human-machine interfaces involving prolonged monitoring or visual cognitive processing, 4-12 degrees/s represents a relatively appropriate speed range for dynamic symbols." (p. 9)

- **Constraint/Pattern**: Cognitive Resource-Bounded Demand-Supply Trade-off Pattern
- **Implication**: Elevating visual presentation velocity increases the cognitive demand required to track dynamic elements, directly reducing the spare attentional supply available for supervisory control while leaving structural context comprehension unchanged.
> **Evidence**: "the level of situational awareness demand increased with speeds over 8 degrees/s... situational awareness supply levels consistently decreased as speed increased above 8 degrees/s... lastly, the main effect of speed on comprehension was not significant" (p. 7)

### 4. Context Assumptions

- **Assumption**: Cognitive Ability Impairment Above 32°/s Display Speeds
> **Evidence**: "although humans could track motion smoothly at speeds up to 90 degrees/s (Meyer, lasker, and Robinson 1985), speeds exceeding 32 degrees/s on the screen may significantly impair cognitive abilities" (p. 2)

- **Assumption**: Inappropriateness of Direct Physical Speed Replication in HMI Design
> **Evidence**: "accurately depicting the speed of a moving fluid symbol in the interface with its actual speed would induce cognitive errors." (p. 2)

