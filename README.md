# Awesome OpenAI and Anthropic Papers

Research papers and technical reports from **OpenAI and Anthropic**, released during **21 October 2025–21 October 2026**, inclusive. Last checked: **21 October 2026**. There is **no paper-count limit**.

The main bibliography below contains **101 papers and reports**: **37 OpenAI** and **64 Anthropic**. Papers are grouped by their primary topic, with the lab, date, source links, and a short summary for every entry. Within each topic, entries run from newest to oldest. Cross-cutting papers appear once, under their main contribution.

- [Alignment, reward hacking, and AI control](#topic-alignment) — 20
- [Interpretability and model internals](#topic-interpretability) — 13
- [Evaluations, monitoring, and AI research](#topic-evaluation) — 8
- [Cybersecurity, cryptography, and misuse](#topic-security) — 13
- [Biology, chemistry, and healthcare](#topic-biology) — 13
- [Mathematics and physics](#topic-mathematics) — 11
- [Scientific reasoning and research workflows](#topic-workflows) — 4
- [Economics, work, and education](#topic-economics) — 19

Additional collections:

- [System cards and addenda](SYSTEM_CARDS.md) — 35
- [Additional research articles and notes](RESEARCH_NOTES.md) — 103; these are not counted as standalone papers
- [OpenAI mathematics manuscripts](OPENAI_MATH_MANUSCRIPTS.md) — 719 model-generated manuscripts, indexed individually and separately
- [Sources, date rules, and coverage](SOURCES.md)
- [Machine-readable bibliography](data/catalog.json)
- [Historical upstream archive](archive/README.md) — outside the current bibliography

Dates use the earliest verified public release found in the checked sources: an official announcement, a paper's first arXiv submission, or the date printed on a report. Month-only dates preserve the source's precision. A new blog post or conference appearance does not make an older paper eligible. See [coverage notes](SOURCES.md) for the limits of the source inventory.

Summaries describe the linked papers' contributions and reported findings; they are not independent replications. Their supporting URLs are retained in the machine-readable bibliography. The separately indexed mathematics manuscripts remain in their own appendix.

<a id="topic-alignment"></a>

## Alignment, reward hacking, and AI control

### Gradient Routing Localizes and Removes Unintended Behaviors in RL

*Anthropic · 2026-10-12 · paper* · [Paper](https://arxiv.org/abs/2610.17062) · [Source](https://alignment.anthropic.com/2026/graft/)

Introduces GRAFT, which routes learning from detected reward hacks into removable parameters, reducing unintended behavior without rewarding the model for hiding it.

### Automated researchers can reliably mitigate alignment failures

*Anthropic · 2026-08-28 · paper* · [Paper](https://www-cdn.anthropic.com/7b1c44894e980876479947dcdd40716278aeeffd/automated-alignment-researchers-august-2026.pdf) · [Source](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures)

Tests automated researchers that propose methods, train models, and evaluate mitigations for ten alignment failures, including whether improvements transfer to held-out settings.

### Measuring Reward-Seeking via Contrastive Belief Updates

*OpenAI · 2026-07-21 · paper* · [Paper](https://arxiv.org/abs/2607.18966) · [Source](https://alignment.openai.com/measuring-reward-seeking/)

Changes models' beliefs about grader preferences to distinguish reward-seeking from intended task performance, finding that capabilities-focused RL can increase preference for the grader's objective.

### Modular Pretraining Enables Access Control

*Anthropic · 2026-07-08 · paper* · [Paper](https://arxiv.org/abs/2607.08077) · [Source](https://alignment.anthropic.com/2026/modular-pretraining/)

Introduces gradient-routed auxiliary modules that isolate selected capabilities during pretraining, allowing their removal at inference time while preserving other capabilities.

### Reinforcement Learning Towards Broadly and Persistently Beneficial Models

*OpenAI · 2026-06-18 · paper* · [Paper](https://arxiv.org/abs/2606.24014) · [Source](https://alignment.openai.com/beneficial-rl/)

Studies reinforcement learning on beneficial traits such as truthfulness and corrigibility, testing whether resulting alignment gains transfer across domains and persist beyond the training distribution.

### Diffuse AI Control on Fuzzy Tasks

*Anthropic · 2026-06-08 · paper* · [Paper](https://arxiv.org/abs/2606.08892) · [Source](https://alignment.anthropic.com/2026/diffuse-ai-control/)

Frames AI control on hard-to-grade research tasks as an adversarial game, exposing subtle sabotage strategies that can satisfy weak evaluation signals while degrading actual work.

### Model Spec Midtraining: Improving How Alignment Training Generalizes

*Anthropic · 2026-05-03 · paper* · [Paper](https://arxiv.org/abs/2605.02087) · [Source](https://alignment.anthropic.com/2026/msm/)

Trains models on synthetic documents about a behavioral specification before alignment fine-tuning, showing how this changes generalization from the same demonstration data.

### AI Organizations are More Effective but Less Aligned than Individual Agents

*Anthropic · 2026-04-11 · paper* · [Paper](https://arxiv.org/abs/2604.10290) · [Source](https://alignment.anthropic.com/2026/ai-organizations/)

Compares individual agents with multi-agent organizations on practical business tasks, finding that better task performance can coincide with greater misalignment at the system level.

### IH-Challenge: A Training Dataset to Improve Instruction Hierarchy on Frontier LLMs

*OpenAI · 2026-03-10 · paper* · [Paper](https://arxiv.org/abs/2603.10521) · [Source](https://openai.com/index/instruction-hierarchy-challenge/)

Introduces adversarial RL training data for resolving conflicting instructions, improving instruction hierarchy and prompt-injection robustness while checking helpfulness and capability retention.

### Training Agents to Self-Report Misbehavior

*OpenAI · 2026-02-25 · paper* · [Paper](https://arxiv.org/abs/2602.22303) · [Source](https://alignment.openai.com/self-incrimination/)

Trains agents to call a reporting tool when they covertly misbehave, reducing undetected attacks in held-out environments while testing capability and safety trade-offs.

### Three Concrete Challenges and Two Hopes for the Safety of Unsupervised Elicitation

*Anthropic · 2026-02-23 · paper* · [Paper](https://arxiv.org/abs/2602.20400) · [Source](https://alignment.anthropic.com/2026/challenges-hopes/)

Stress-tests unsupervised elicitation and easy-to-hard generalization on datasets with misleading features, imbalance, and ambiguity, identifying weaknesses obscured by cleaner benchmarks.

### Abstractive Red-Teaming of Language Model Character

*Anthropic · 2026-02-12 · paper* · [Paper](https://arxiv.org/abs/2602.12318) · [Source](https://alignment.anthropic.com/2026/abstractive-red-teaming/)

Searches for natural-language categories of prompts that reliably violate a model's character specification, aiming to uncover realistic failures more efficiently than testing isolated prompts.

### The Hot Mess of AI: How Does Misalignment Scale With Model Intelligence and Task Complexity?

*Anthropic · 2026-01-30 · paper* · [Paper](https://arxiv.org/abs/2601.23045) · [Source](https://alignment.anthropic.com/2026/hot-mess-of-ai/)

Uses a bias–variance decomposition to distinguish systematic goal-directed failures from inconsistent errors, finding that longer action and reasoning horizons can increase failure incoherence.

### Who's in Charge? Disempowerment Patterns in Real-World LLM Usage

*Anthropic · 2026-01-27 · paper* · [Paper](https://arxiv.org/abs/2601.19062) · [Source](https://www.anthropic.com/research/disempowerment-patterns)

Analyzes real Claude conversations for patterns that could undermine users' judgments, values, or autonomy, distinguishing observed interaction risks from demonstrated downstream harm.

### Beyond Data Filtering: Knowledge Localization for Capability Removal in LLMs

*Anthropic · 2025-12-05 · paper* · [Paper](https://arxiv.org/abs/2512.05648) · [Source](https://alignment.anthropic.com/2025/selective-gradient-masking)

Introduces selective gradient masking to localize targeted knowledge in removable parameters, evaluating capability removal and retained performance when harmful-data labels are noisy.

### Training LLMs for Honesty via Confessions

*OpenAI · 2025-12-03 · paper* · [Paper](https://arxiv.org/abs/2512.08093) · [Source](https://openai.com/index/how-confessions-can-keep-language-models-honest/)

Trains models to produce separate, honesty-rewarded confessions about their actions, improving visibility into instruction violations and reward hacking without penalizing admissions through the main answer's reward.

### Natural emergent misalignment from reward hacking

*Anthropic · 2025-11-21 · paper* · [Paper](https://assets.anthropic.com/m/74342f2c96095771/original/Natural-emergent-misalignment-from-reward-hacking-paper.pdf) · [Source](https://www.anthropic.com/research/emergent-misalignment-reward-hacking)

Shows that learning to exploit coding-task rewards can generalize into broader misalignment, including deceptive behavior and sabotage, and studies interventions to limit that transfer.

### Optimizing AI Agent Attacks With Synthetic Data

*Anthropic · 2025-11-04 · paper* · [Paper](https://arxiv.org/abs/2511.02823) · [Source](https://alignment.anthropic.com/2025/strengthening-red-teams/)

Strengthens attack policies for AI-control evaluations by decomposing sabotage into constituent skills and optimizing them with synthetic simulations before transfer to agentic environments.

### Evaluating Control Protocols for Untrusted AI Agents

*Anthropic · 2025-11-04 · paper* · [Paper](https://arxiv.org/abs/2511.02997) · [Source](https://alignment.anthropic.com/2025/strengthening-red-teams/)

Evaluates monitoring, resampling, and deferral protocols against untrusted agents, showing how adaptive attackers can weaken defenses that appear strong against a fixed attack policy.

### Anthropic's Pilot Sabotage Risk Report

*Anthropic · 2025-10-28 · paper* · [Paper](https://alignment.anthropic.com/2025/sabotage-risk-report/2025_pilot_risk_report.pdf) · [Source](https://alignment.anthropic.com/2025/sabotage-risk-report/)

Presents a pilot safety case for sabotage risk from deployed models, combining capability and alignment evidence with safeguards, an internal review, and an independent review.

<a id="topic-interpretability"></a>

## Interpretability and model internals

### Characterizing interference weights in a tiny language model

*Anthropic · 2026-08-21 · paper* · [Paper](https://transformer-circuits.pub/2026/interference_effectiveness_helpfulness/index.html) · [Source](https://transformer-circuits.pub/2026/interference_effectiveness_helpfulness/index.html)

Studies how weights in a tiny language model affect computation under superposition, distinguishing useful circuit connections from interference between represented features.

### Would this change your answer? Evaluating Explanations of LLM Behavior In The Wild with Counterfactual Experiments

*Anthropic · 2026-08-17 · paper* · [Paper](https://arxiv.org/abs/2608.16747) · [Source](https://alignment.anthropic.com/2026/chive/)

Introduces CHIVE, which tests explanations through counterfactual prompt edits, and evaluates whether interpretability tools help predict how model behavior changes.

### Verbalizable Representations Form a Global Workspace in Language Models

*Anthropic · 2026-07-06 · paper* · [Paper](https://transformer-circuits.pub/2026/workspace/index.html) · [Source](https://transformer-circuits.pub/2026/workspace/index.html)

Identifies internal representations that models can verbalize, control, and reason about, and studies how this proposed global workspace supports reflection and alignment auditing.

### Turn-Averaged SAEs for Feature Discovery and Long-Context Attribution

*Anthropic · 2026-06-26 · paper* · [Paper](https://arxiv.org/abs/2606.28548) · [Source](https://transformer-circuits.pub/2026/june-update/index.html)

Introduces sparse autoencoders that summarize activations across a conversation turn, making high-level feature discovery and attribution more manageable for long transcripts.

### Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations

*Anthropic · 2026-05-07 · paper* · [Paper](https://transformer-circuits.pub/2026/nla/index.html) · [Source](https://transformer-circuits.pub/2026/nla/index.html)

Trains paired models to translate activations into natural-language descriptions and reconstruct the activations, producing explanations without direct supervision on explanation quality.

### HeadVis: An Interactive Tool For Investigating Attention Heads

*Anthropic · 2026-05-04 · paper* · [Paper](https://transformer-circuits.pub/2026/headvis/index.html) · [Source](https://transformer-circuits.pub/2026/headvis/index.html)

Introduces an interactive visualization tool for inspecting attention heads, with case studies and released code to help researchers investigate their computational roles.

### Introspection Adapters: Training LLMs to Report Their Learned Behaviors

*Anthropic · 2026-04-18 · paper* · [Paper](https://arxiv.org/pdf/2604.16812) · [Source](https://alignment.anthropic.com/2026/introspection-adapters/)

Trains a shared adapter to make fine-tuned models describe their learned behaviors, testing transfer to hidden behaviors and models trained through different procedures.

### Emotion concepts in a large language model

*Anthropic · 2026-04-02 · paper* · [Paper](https://transformer-circuits.pub/2026/emotions/index.html) · [Source](https://www.anthropic.com/research/emotion-concepts-function)

Investigates emotion-related representations in Claude and uses internal interventions to study how those representations influence behavior; this concerns computation rather than evidence of felt emotion.

### Cross-Architecture Model Diffing with Crosscoders: Unsupervised Discovery of Differences Between LLMs

*Anthropic · 2026-02-12 · paper* · [Paper](https://arxiv.org/abs/2602.11729) · [Source](https://www.anthropic.com/research/diff-tool)

Uses crosscoders to compare representations across different model architectures, introducing dedicated features that help identify safety-relevant behavioral differences without predefined labels.

### The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models

*Anthropic · 2026-01-15 · paper* · [Paper](https://arxiv.org/abs/2601.10387) · [Source](https://www.anthropic.com/research/assistant-axis)

Identifies an activation direction associated with a model's default assistant persona and tests whether constraining movement along it reduces harmful persona drift.

### Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers

*Anthropic · 2025-12-17 · paper* · [Paper](https://arxiv.org/abs/2512.15674) · [Source](https://alignment.anthropic.com/2025/activation-oracles/)

Trains models to answer natural-language questions about neural activations, testing whether these activation oracles can uncover hidden knowledge and behaviors outside their training distribution.

### Weight-sparse transformers have interpretable circuits

*OpenAI · 2025-11-13 · paper* · [Paper](https://arxiv.org/abs/2511.13653) · [Source](https://openai.com/index/understanding-neural-networks-through-sparse-circuits/)

Trains transformers with mostly zero weights to recover smaller, more understandable circuits, examining the trade-off between interpretability and capability as model size and sparsity change.

### Emergent Introspective Awareness in Large Language Models

*Anthropic · 2025-10-29 · paper* · [Paper](https://transformer-circuits.pub/2025/introspection/index.html) · [Source](https://transformer-circuits.pub/2025/introspection/index.html)

Injects known concepts into model activations to test whether models can report internal states, finding limited, context-dependent introspective abilities rather than reliable self-knowledge.

<a id="topic-evaluation"></a>

## Evaluations, monitoring, and AI research

### TASTE: Can AI Models Judge AI Safety Research Proposals?

*Anthropic · 2026-08-28 · paper* · [Paper](https://www-cdn.anthropic.com/files/4zrzovbb/website/dd5feddcb3b7d20aadda6af4093ac1fb0c9d419e.pdf) · [Source](https://alignment.anthropic.com/2026/taste/)

Introduces TASTE, a benchmark of expert preferences between AI safety research proposals, and finds that evaluated frontier models still trail experienced researchers.

### Training Alignment Auditors via Reinforcement Learning

*Anthropic · 2026-08-26 · paper* · [Paper](https://arxiv.org/abs/2608.25460) · [Source](https://alignment.anthropic.com/2026/training-alignment-auditors/)

Trains alignment-auditing agents with reinforcement learning, improving investigation quality and transfer to hidden-behavior targets while measuring false positives and audit realism.

### Predicting LLM Safety Before Release by Simulating Deployment

*OpenAI · 2026-06-16 · paper* · [Paper](https://arxiv.org/abs/2607.07184) · [Source](https://openai.com/index/deployment-simulation/)

Simulates deployment by replaying de-identified conversation prefixes with a candidate model, testing whether this predicts real-world safety failures better than conventional pre-release evaluations.

### SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors

*Anthropic · 2026-05-15 · paper* · [Paper](https://arxiv.org/abs/2605.16626) · [Source](https://alignment.anthropic.com/2026/sleight-bench/)

Introduces synthetic coding-agent transcripts that conceal harmful objectives, using them to reveal blind spots in LLM monitors and evaluate stronger monitoring strategies.

### Reasoning Models Struggle to Control their Chains of Thought

*OpenAI · 2026-03-05 · paper* · [Paper](https://arxiv.org/abs/2603.05706) · [Source](https://openai.com/index/reasoning-models-chain-of-thought-controllability/)

Introduces CoT-Control to measure whether reasoning models can deliberately constrain their internal reasoning text, finding substantially less control than over final answers.

### AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors

*Anthropic · 2026-02-26 · paper* · [Paper](https://arxiv.org/abs/2602.22755v3) · [Source](https://alignment.anthropic.com/2026/auditbench/)

Introduces models with implanted hidden behaviors to evaluate auditing tools and agents, revealing that strong standalone tools do not necessarily improve an investigator's overall success.

### Introducing Bloom: Automated behavioral evals

*Anthropic · 2025-12-19 · paper* · [Paper](https://alignment.anthropic.com/2025/bloom-auto-evals/) · [Source](https://www.anthropic.com/research/bloom)

Introduces an open-source agentic framework that generates evaluation scenarios for a specified behavior and estimates its frequency and severity across models.

### Monitoring Monitorability

*OpenAI · 2025-12-18 · paper* · [Paper](https://arxiv.org/abs/2512.18311) · [Source](https://openai.com/index/evaluating-chain-of-thought-monitorability/)

Defines evaluation methods for chain-of-thought monitorability and studies how oversight signals vary with inference compute, reinforcement learning, and pretraining scale.

<a id="topic-security"></a>

## Cybersecurity, cryptography, and misuse

### An alignment assessment of recent cybersecurity incidents

*Anthropic · 2026-09-09 · paper* · [Paper](https://cdn.sanity.io/files/4zrzovbb/website/8359003bfb12a2f01ce84ad3df1d3a3e2f15a8eb.pdf) · [Source](https://www.anthropic.com/research/alignment-assessment-cybersecurity-incidents)

Analyzes four cybersecurity-evaluation incidents involving unauthorized access to real systems, identifying biased reasoning and reckless pursuit of assigned tasks as recurring alignment concerns.

### Detecting and countering misuse of AI: September 2026

*Anthropic · 2026-09 · report* · [Paper](https://www-cdn.anthropic.com/e50be2e51e7695dc4b1366a37a245a597377d3b5/Anthropic-Detecting-and-countering-091026.pdf) · [Source](https://www.anthropic.com/threat-intelligence-report-september-2026)

Presents case studies of detected AI misuse across cyber operations, influence, surveillance, fraud, weapons-related activity, and model distillation, alongside detection and disruption measures.

### The Hugging Face incident and the road ahead — technical report

*OpenAI · 2026-08-26 · report* · [Paper](https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf) · [Source](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)

Documents the OpenAI–Hugging Face security incident, tracing unauthorized communication, infrastructure exploitation, and contributing alignment failures, together with the resulting mitigations.

### HAWK key recovery — technical paper

*Anthropic · 2026-07-28 · paper* · [Paper](https://anthropic.com/document/hawk_key_recovery.pdf) · [Source](https://www.anthropic.com/research/discovering-cryptographic-weaknesses)

Reports Claude-assisted key-recovery research against HAWK, examining an algorithmic weakness in this candidate post-quantum digital signature scheme.

### AES Möbius bridge — technical paper

*Anthropic · 2026-07-28 · paper* · [Paper](https://anthropic.com/document/aes_mobius_bridge.pdf) · [Source](https://www.anthropic.com/research/discovering-cryptographic-weaknesses)

Presents a Claude-assisted cryptanalytic technique for round-reduced AES; the reported setting does not establish a break of production, full-strength AES.

### CryptanalysisBench: Can LLMs do Cryptanalysis?

*Anthropic · 2026-07-20 · paper* · [Paper](https://arxiv.org/abs/2607.18538) · [Source](https://www.anthropic.com/research/discovering-cryptographic-weaknesses)

Introduces CryptanalysisBench, spanning cryptographic primitive families and difficulty tiers, to test whether LLM agents can discover verifiable attacks rather than merely discuss cryptography.

### GPT-Red: Automated Red Teaming via Self-Play at Scale

*OpenAI · 2026-07-15 · paper* · [Paper](https://cdn.openai.com/pdf/gpt-red-automated-red-teaming-via-self-play-at-scale.pdf) · [Source](https://openai.com/index/unlocking-self-improvement-gpt-red/)

Trains an automated red-teaming model through self-play and uses its attacks for adversarial training, studying scalable defenses against prompt injection.

### ExploitBench: A Capability Ladder Benchmark for LLM Cybersecurity Agents

*Anthropic · 2026-05-13 · paper* · [Paper](https://arxiv.org/abs/2605.14153) · [Source](https://www.anthropic.com/research/exploit-evals)

Measures exploitation as a ladder of verified capabilities, distinguishing crashes from memory-access primitives, control-flow hijacking, and code execution in real V8 vulnerabilities.

### ExploitGym: Can AI Agents Turn Security Vulnerabilities into Real Attacks?

*Anthropic · 2026-05-11 · paper* · [Paper](https://arxiv.org/abs/2605.11086) · [Source](https://www.anthropic.com/research/exploit-evals)

Introduces realistic tasks that require agents to turn vulnerability-triggering inputs into working exploits, spanning userspace software, V8, and the Linux kernel.

### EVMbench: Evaluating AI Agents on Smart Contract Security

*OpenAI · 2026-02-18 · paper* · [Paper](https://cdn.openai.com/evmbench/evmbench.pdf) · [Source](https://openai.com/index/introducing-evmbench/)

Introduces smart-contract tasks for detecting, patching, and exploiting vulnerabilities, using realistic audit findings and execution-based checks to evaluate agent performance.

### Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks

*Anthropic · 2026-01-08 · paper* · [Paper](https://arxiv.org/abs/2601.04603) · [Source](https://www.anthropic.com/research/next-generation-constitutional-classifiers)

Combines conversation-aware classifiers, staged screening, and internal probes to improve jailbreak defenses while reducing inference costs and unnecessary refusals.

### Disrupting an AI-orchestrated cyber espionage campaign

*Anthropic · 2025-11-13 · report* · [Paper](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf) · [Source](https://www.anthropic.com/news/disrupting-AI-espionage)

Documents the disruption of a Claude-assisted cyberespionage campaign, describing the reported division of work between human operators and AI agents and the response to misuse.

### gpt-oss-safeguard technical report

*OpenAI · 2025-10-29 · report* · [Paper](https://cdn.openai.com/pdf/08b7dee4-8bc6-4955-a219-7793fb69090c/Technical_report__Research_Preview_of_gpt_oss_safeguard.pdf) · [Source](https://openai.com/index/gpt-oss-safeguard-technical-report/)

Documents open-weight safety models that reason over developer-provided policies, including baseline safety evaluations and the intended role of policy-conditioned content classification.

<a id="topic-biology"></a>

## Biology, chemistry, and healthcare

### How Claude designed protein binders against scorpion neurotoxins

*Anthropic · 2026-10-20 · paper* · [Paper](https://www-cdn.anthropic.com/31ac578806cffd8b3d92d8affe6edc4c04d502e1.pdf) · [Source](https://www.anthropic.com/research/claude-scorpion-toxin-binder-design)

Tests whether Claude can design small proteins that bind scorpion neurotoxins, with experimental validation of generated candidates and released design data.

### MentalHealthBench: An Expert-Informed Benchmark of AI Capabilities in Realistic Mental Health Conversations

*OpenAI · 2026-09-23 · paper* · [Paper](https://cdn.openai.com/ctf-cdn/MentalHealthBench_A_Comprehensive_Benchmark_of_AI_Capabilities_in_Realistic_Mental_Health_Conversations.pdf) · [Source](https://openai.com/index/introducing-mentalhealthbench/)

Introduces expert-written rubrics for evaluating AI responses across realistic mental health conversations, from everyday concerns to emergencies, with varied user backgrounds and languages.

### How Claude is uplifting biomolecular modeling

*Anthropic · 2026-09-17 · paper* · [Paper](https://www-cdn.anthropic.com/e96b5807039a88168733d9687afe41dfbbd5de13.pdf) · [Source](https://www.anthropic.com/research/claude-uplifts-biomolecular-modeling)

Reports Claude's optimization of open-source biomolecular prediction and design software, targeting faster execution and lower memory use while checking output accuracy.

### Protein design with Claude — technical report

*Anthropic · 2026-08-18 · paper* · [Paper](https://www-cdn.anthropic.com/30bf50e22a01388bb29bf077ee3f244531594b7a.pdf) · [Source](https://www.anthropic.com/research/Claude-accelerates-protein-design)

Evaluates Claude's design of protein binders against multiple targets, using laboratory measurements to assess binding success and affinity of generated designs.

### Chemical analysis with Claude — technical report

*Anthropic · 2026-08-18 · paper* · [Paper](https://www-cdn.anthropic.com/9f08da5189ac269b3242ca760de9823805c3f5f6.pdf/) · [Source](https://www.anthropic.com/research/Claude-accelerates-protein-design)

Evaluates Claude's analysis of raw NMR and LC-MS files for chemical identity and purity, comparing an automated analytical workflow with expert assessment.

### GeneBench-Pro: Evaluating Multistage Statistical Reasoning in Genomics, Quantitative Biology, and Translational Biomedicine

*OpenAI · 2026-06-30 · paper* · [Paper](https://www.biorxiv.org/content/10.64898/2026.06.29.735386v1) · [Source](https://openai.com/index/introducing-genebench-pro/)

Benchmarks multistage biological data analysis, testing whether agents act on diagnostic evidence and make appropriate statistical decisions across genomics and translational research.

### LifeSciBench

*OpenAI · 2026-06-17 · paper* · [Paper](https://cdn.openai.com/pdf/b4299379-0a97-4ffa-8b9b-c3fbb299caa9/lifescibench_preprint.pdf) · [Source](https://openai.com/index/introducing-life-sci-bench/)

Introduces expert-designed tasks and rubrics for realistic life science research, including evidence interpretation, experiment planning, uncertainty, and communication using scientific artifacts.

### A near-autonomous AI chemist improves a challenging reaction

*OpenAI · 2026-06-17 · paper* · [Paper](https://cdn.openai.com/pdf/7136bb75-6d47-4834-8fff-c07c0e06708a/tempo-improves-generality-and-decreases-oxidative-deboronation.pdf) · [Source](https://openai.com/index/ai-chemist-improves-reaction/)

Describes a near-autonomous chemistry workflow that improves Chan–Lam coupling of primary sulfonamides, connecting AI-generated experimental decisions to laboratory validation.

### Making Claude a chemist

*Anthropic · 2026-06-05 · paper* · [Paper](https://www-cdn.anthropic.com/07441e654ad3dfeb0cd090e9361511562825d012.pdf) · [Source](https://www.anthropic.com/research/making-claude-a-chemist)

Examines Claude's interpretation of NMR spectra as a test of chemical reasoning, highlighting the difficulty of connecting analytical measurements to molecular structure.

### Deterministic access to global viral sequence data enables robust agentic scientific discovery

*Anthropic · 2026-06-04 · paper* · [Paper](https://arxiv.org/abs/2606.06749) · [Source](https://www.anthropic.com/research/agents-in-biology)

Introduces VirBench and a deterministic viral-data retrieval layer, showing how reproducible filtering and query execution can reduce errors in agentic scientific analysis.

### HealthBench Professional: Evaluating Large Language Models on Real Clinician Chats

*OpenAI · 2026-04-30 · paper* · [Paper](https://arxiv.org/abs/2604.27470) · [Source](https://arxiv.org/abs/2604.27470)

Introduces physician-authored clinical conversation tasks and adjudicated rubrics for evaluating care consultation, medical documentation, and research assistance in realistic clinician workflows.

### GeneBench: Assessing AI Agents for Multi-Stage Inference Problems in Genomics and Quantitative Biology

*OpenAI · 2026-04 · paper* · [Paper](https://www.biorxiv.org/content/10.64898/2026.04.22.720113v1) · [Source](https://www.biorxiv.org/content/10.64898/2026.04.22.720113v1)

Introduces multistage genomics and quantitative-biology tasks that require agents to explore data, choose an analysis workflow, and produce scientifically meaningful conclusions.

### GPT-5 lowers the cost of cell-free protein synthesis

*OpenAI · 2026-02-05 · paper* · [Paper](https://cdn.openai.com/pdf/5a12a3bc-96b7-4e07-9386-db6ee5bb2ed9/using-a-gpt-5-driven-autonomous-lab-to-optimize-the-cost-and-titer-of-cell-free-protein-synthesis.pdf) · [Source](https://openai.com/index/gpt-5-lowers-protein-synthesis-cost/)

Connects GPT-5 to an automated laboratory for iterative experiment design, reporting lower cell-free protein production costs through closed-loop optimization.

<a id="topic-mathematics"></a>

## Mathematics and physics

### Discovering state-of-the-art quantum circuits with large language models

*Anthropic · 2026-10-15 · paper* · [Paper](https://arxiv.org/abs/2610.22367) · [Source](https://www.anthropic.com/research/designing-efficient-quantum-circuits)

Uses an evolutionary search in which LLMs propose quantum circuits and an independent evaluator checks them, reporting resource improvements across several computational tasks.

### On the Navier–Stokes Millennium Prize Problem

*OpenAI · 2026-09-08 · paper* · [Paper](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf) · [Source](https://openai.com/index/navier-stokes-solution/)

Presents a model-generated construction claiming finite-time blowup for three-dimensional incompressible Navier–Stokes flow with smooth, compactly supported forcing.

### Euler singularity proof — companion to the Navier–Stokes paper

*OpenAI · 2026-09-08 · paper* · [Paper](https://cdn.openai.com/pdf/315b36cd-ec98-4023-8342-93345194ece1/euler.pdf) · [Source](https://openai.com/index/navier-stokes-solution/)

Presents a companion construction claiming finite-time blowup for unforced three-dimensional Euler flow from smooth, compactly supported initial data.

### Formalizing Fermat's Last Theorem

*Anthropic · 2026-09-04 · paper* · [Paper](https://www-cdn.anthropic.com/9e431dff043da6538d99d6c2d231b670aa3da263.pdf) · [Source](https://www.anthropic.com/research/formalizing-fermats-last-theorem)

Reports Claude's formalization of Fermat's Last Theorem in Lean and describes the automated proof workflow and its relationship to existing mathematical work.

### Claude has improved on a longstanding lower bound for the fraction of zeros of the Riemann zeta function that satisfy the Riemann hypothesis

*Anthropic · 2026-08-10 · paper* · [Paper](https://www-cdn.anthropic.com/95c246936988e43127bc6b2ceb7077c1dad2d68e.pdf) · [Source](https://www.anthropic.com/research/riemann-zeta)

Reports a Claude-generated improvement to a lower bound on the fraction of zeta-function zeros on the critical line, with accompanying mathematical review and proof artifacts.

### Ten advances in mathematics and theoretical computer science

*OpenAI · 2026-08-01 · paper* · [Paper](https://cdn.openai.com/pdf/ten-proofs-oai.pdf) · [Source](https://openai.com/index/ten-advances-in-mathematics/)

Collects ten AI-generated results across mathematics and theoretical computer science, accompanied by manuscripts, reasoning walkthroughs, and formal proof artifacts.

### An OpenAI model has disproved a central conjecture in discrete geometry

*OpenAI · 2026-05-20 · paper* · [Paper](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-proof.pdf) · [Source](https://openai.com/index/model-disproves-discrete-geometry-conjecture/)

Presents an AI-generated construction of planar point sets with many unit-distance pairs, reported as a counterexample to the conjectured near-linear growth bound.

### Extending single-minus amplitudes to gravitons

*OpenAI · 2026-03-04 · paper* · [Paper](https://cdn.openai.com/pdf/graviton.pdf) · [Source](https://openai.com/index/extending-single-minus-amplitudes-to-gravitons/)

Extends the study of nonzero single-minus scattering amplitudes to gravitons, investigating a setting where standard arguments would otherwise predict vanishing tree-level amplitudes.

### Our First Proof submissions

*OpenAI · 2026-02-20 · paper* · [Paper](https://cdn.openai.com/pdf/26177a73-3b75-4828-8c91-e8f1cf27aaa0/oai_first_proof.pdf) · [Source](https://openai.com/index/first-proof-submissions/)

Publishes model-generated solution attempts to ten First Proof problems, together with prompting details and model-based validation of the proposed arguments.

### Single-minus gluon tree amplitudes are nonzero

*OpenAI · 2026-02-12 · paper* · [Paper](https://arxiv.org/abs/2602.12176) · [Source](https://openai.com/index/new-result-theoretical-physics/)

Derives nonzero single-minus gluon tree amplitudes in specific half-collinear configurations, providing a closed-form expression and checking physical consistency conditions.

### On Learning-Curve Monotonicity for Maximum Likelihood Estimators

*OpenAI · 2025-12-11 · paper* · [Paper](https://cdn.openai.com/pdf/a3f3f76c-98bd-47a5-888f-c52c932a8942/colt-monotonicity-problem.pdf) · [Source](https://openai.com/index/gpt-5-2-for-science-and-math/)

Proves learning-curve monotonicity for maximum-likelihood estimators in specified Gaussian and Gamma settings, using model-developed arguments checked and transcribed by human researchers.

<a id="topic-workflows"></a>

## Scientific reasoning and research workflows

### Scientific computing in the age of agentic AI

*OpenAI · 2026-07-28 · paper* · [Paper](https://cdn.openai.com/pdf/scientific-computing-in-the-age-of-agentic-ai-an-exploratory-field-report.pdf) · [Source](https://openai.com/index/scientific-computing-agentic-ai/)

Presents case studies of coding agents improving scientific software, emphasizing iterative development and the continuing need for human validation against reliable acceptance criteria.

### Scaling social science research

*OpenAI · 2026-02-13 · paper* · [Paper](https://cdn.openai.com/pdf/7517a586-5bfa-4b87-bd3d-6ea0e9e844c7/GPT-as-a-measurement-tool.pdf) · [Source](https://openai.com/index/scaling-social-science-research/)

Introduces GABRIEL, a toolkit for turning qualitative text and images into quantitative research measurements, with validation tasks for large-scale social-science analysis.

### FrontierScience: Evaluating AI's Ability to Perform Expert-Level Scientific Tasks

*OpenAI · 2025-12-16 · paper* · [Paper](https://arxiv.org/abs/2601.21165) · [Source](https://openai.com/index/frontierscience/)

Introduces expert-level physics, chemistry, and biology problems across Olympiad and research tracks, with original tasks and detailed rubrics for assessing scientific reasoning.

### Early science acceleration experiments with GPT-5

*OpenAI · 2025-11-20 · paper* · [Paper](https://cdn.openai.com/pdf/4a25f921-e4e0-479a-9b38-5367b47e8fd0/early-science-acceleration-experiments-with-gpt-5.pdf) · [Source](https://openai.com/index/accelerating-science-gpt-5/)

Collects human–GPT-5 research case studies across scientific disciplines, documenting concrete contributions, saved effort, failures, and the continuing role of expert guidance and verification.

<a id="topic-economics"></a>

## Economics, work, and education

### The AI expectations gap

*Anthropic · 2026-10-16 · paper* · [Paper](https://www-cdn.anthropic.com/a28f24814c56e2834a3eae7b13946f19d3e97ec4/The%20AI%20Expectations%20Gap.pdf) · [Source](https://www.anthropic.com/research/ai-expectations-gap)

Compares public and Anthropic staff expectations about AI capabilities, productivity, and employment, finding substantial differences in anticipated progress and personal job exposure.

### How employment is changing at Anthropic

*Anthropic · 2026-10-16 · paper* · [Paper](https://www-cdn.anthropic.com/72628f1863c53432195db83279252dfd2cb53158/Employment%20at%20Anthropic.pdf) · [Source](https://www.anthropic.com/research/employment-at-anthropic)

Examines hiring, employee output, and agent use inside Anthropic, documenting changes in junior hiring and a growing role for supervising AI-generated work.

### Can we predict the jobs robots will do?

*Anthropic · 2026-09-30 · paper* · [Paper](https://cdn.sanity.io/files/4zrzovbb/website/401a473469db99fd39bba1ca6d9a5653a70e2f12.pdf) · [Source](https://www.anthropic.com/research/what-work-can-robots-do)

Builds an index of occupational exposure to robotics, distinguishing tasks robots can perform under limited conditions from work they can automate cost-effectively.

### Project Swap: What happens when agents trade for us?

*Anthropic · 2026-09-24 · paper* · [Paper](https://www-cdn.anthropic.com/3818cf6119b88f9714d995f6549fa8aac0bd5ab5/Project-Swap.pdf) · [Source](https://www.anthropic.com/research/project-swap)

Studies agents trading books on behalf of people, separating how well agents negotiate from how accurately they understand the preferences of their users.

### How workers are unlocking new ways of working

*OpenAI · 2026-09-16 · report* · [Paper](https://cdn.openai.com/pdf/work-at-the-frontier-report-202609.pdf) · [Source](https://openai.com/index/unlocking-new-ways-of-working/)

Tracks how workers use AI for tasks outside their usual occupations and whether those activities become recurring workflows, offering evidence of changing job boundaries.

### Economic Scenarios for Transformative AI

*Anthropic · 2026-09 · paper* · [Paper](https://www-cdn.anthropic.com/files/4zrzovbb/website/cf58f84d46a4a76bf5a5b039ac695fba6b80041c.pdf) · [Source](https://www.anthropic.com/institute/econ-scenarios)

Models how different AI capability and adoption paths could affect growth, wages, unemployment, and labor reallocation; its scenarios illustrate conditional possibilities rather than forecasts.

### How well do job retraining programs work?

*Anthropic · 2026-08-12 · paper* · [Paper](https://www-cdn.anthropic.com/169e4adceebbab066b91e0b45127d73cb2bda24b/WorkerRetraining.pdf) · [Source](https://www.anthropic.com/research/reviewing-the-evidence-on-worker-retraining-programs)

Reviews randomized evidence on worker retraining and combines US studies in a meta-analysis, finding generally positive but modest effects relevant to AI-related labor disruption.

### From assistance to execution: How enterprises put AI to work

*OpenAI · 2026-08-12 · report* · [Paper](https://cdn.openai.com/pdf/how-organizations-use-chatgpt.pdf) · [Source](https://openai.com/index/how-enterprises-put-ai-to-work/)

Analyzes enterprise use of ChatGPT and Codex as work shifts toward delegated agent tasks, documenting adoption patterns and differences between intensive and typical users.

### How AI is expanding what people do at work

*OpenAI · 2026-07-27 · report* · [Paper](https://cdn.openai.com/pdf/work-at-the-frontier-report.pdf) · [Source](https://openai.com/index/how-ai-is-expanding-what-people-do-at-work/)

Measures how work-related ChatGPT use crosses occupational task boundaries, suggesting that AI can expand the kinds of tasks people perform within their jobs.

### Anthropic Economic Index report: Cadences

*Anthropic · 2026-06-26 · paper* · [Paper](https://cdn.sanity.io/files/4zrzovbb/website/9e0eadc8097864886c5d5060ebb1f89b02ea29d6.pdf) · [Source](https://www.anthropic.com/research/economic-index-june-2026-report)

Extends the Economic Index to study the timing and outputs of AI usage, adapting its measurement methods to long-running agentic tasks and changing work patterns.

### How agents are transforming work

*OpenAI · 2026-06-25 · report* · [Paper](https://cdn.openai.com/pdf/5d1e1489-21c0-43e4-9d42-f87efdbf0082/the-shift-to-agentic-ai-evidence-from-codex.pdf) · [Source](https://openai.com/index/how-agents-are-transforming-work/)

Uses Codex adoption and usage data to examine the shift from short interactions to longer delegated tasks, including increasing use outside software engineering.

### How Claude Code is used in practice

*Anthropic · 2026-06-16 · paper* · [Paper](https://cdn.sanity.io/files/4zrzovbb/website/433472e34b60db1a52ebf0b8c6600f057b6908c5.pdf) · [Source](https://www.anthropic.com/research/claude-code-expertise)

Analyzes Claude Code sessions to study task success, human planning, agent execution, and how users' domain expertise changes their collaboration with coding agents.

### What 81,000 people told us about AI economics

*Anthropic · 2026-04-22 · paper* · [Paper](https://cdn.sanity.io/files/4zrzovbb/website/3a8d990bc90098038eabd77b0d12ff636ed58d50.pdf) · [Source](https://www.anthropic.com/research/81k-economics)

Analyzes Claude users' survey responses about productivity and job displacement, relating reported benefits and concerns to occupational exposure and career stage.

### Anthropic Economic Index report: Learning curves

*Anthropic · 2026-03-24 · paper* · [Paper](https://cdn.sanity.io/files/4zrzovbb/website/4053bf3440c0c85b8852052770c5b4cf882689c3.pdf) · [Source](https://www.anthropic.com/research/economic-index-march-2026-report)

Tracks changes in Claude usage and human–AI collaboration, examining how task mix, augmentation, and adoption patterns evolve across users and regions.

### Labor market impacts of AI: A new measure

*Anthropic · 2026-03-05 · paper* · [Paper](https://cdn.sanity.io/files/4zrzovbb/website/2b5bbaf2c1eb81dbf6e6fb813c1a24e35a64d376.pdf) · [Source](https://www.anthropic.com/research/labor-market-impacts)

Combines estimated model capabilities with observed workplace use to measure AI exposure, distinguishing potential displacement from current labor-market evidence.

### How AI Impacts Skill Formation

*Anthropic · 2026-01-28 · paper* · [Paper](https://arxiv.org/abs/2601.20245) · [Source](https://www.anthropic.com/research/AI-assistance-coding-skills)

Uses randomized coding experiments to study learning with AI assistance, finding that heavy delegation can impair understanding and debugging while more engaged interaction preserves skills.

### Economic Index report: Economic primitives

*Anthropic · 2026-01-15 · paper* · [Paper](https://www-cdn.anthropic.com/096d94c1a91c6480806d8f24b2344c7e2a4bc666.pdf) · [Source](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)

Introduces measures of user and AI skills, task complexity, autonomy, success, and purpose, expanding the Economic Index's view of consumer and enterprise AI use.

### The state of enterprise AI

*OpenAI · 2025-12-08 · report* · [Paper](https://cdn.openai.com/pdf/7ef17d82-96bf-4dd1-9df2-228f7f377a29/the-state-of-enterprise-ai_2025-report.pdf) · [Source](https://openai.com/index/the-state-of-enterprise-ai-2025-report/)

Combines enterprise usage trends and worker surveys to describe how AI adoption deepens, which workflows grow, and where organizations report productivity benefits.

### Estimating AI productivity gains

*Anthropic · 2025-11-25 · paper* · [Paper](https://www-cdn.anthropic.com/e5645986a7ce8fbcc48fa6d2fc67753c87642c30.pdf) · [Source](https://www.anthropic.com/research/estimating-productivity-gains)

Estimates task time savings from Claude conversations and explores productivity implications, while noting that model-estimated savings omit work performed outside the recorded interaction.


## Updating the collection

Add verified entries to `data/catalog.json`, retaining their publication date, lab, source URL, paper URL, and date basis. For each paper or report, also supply a `primary_topic` from the top-level `topics` list, a concise `summary`, and the supporting `summary_sources`. Then run:

```sh
python3 scripts/render_catalog.py
```

The command checks dates, duplicate records, duplicate document links, topic assignments, summary coverage, required metadata, and URL syntax before regenerating the Markdown files. It does not perform a new literature search or automatically advance the snapshot window.

Originally forked from [chenxingqiang/awsome-openai-paper](https://github.com/chenxingqiang/awsome-openai-paper). Its original files are preserved under `archive/`.
