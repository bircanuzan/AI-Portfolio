# Gameplay evaluation task

**Producer brief:** "Holding Space should not instantly finish the pickup objective. Make each deliberate Space keypress collect exactly one token; after three tokens, show an unmistakable completion state."

**Bug reproduction:** Replace main.gd with broken_main.gd. Launch main.tscn. Hold Space for half a second. Observe the counter jump beyond 3 because input is sampled every frame.

**Reference fix:** Restore main.gd. Use Input.is_action_just_pressed; cap collection at TARGET; freeze the score after completion.

**Acceptance criteria**
1. On launch, visual state is "Tokens 0/3".
2. Press and hold Space: counter advances **exactly once** to 1/3, not multiple times.
3. Release and press again twice: counter advances to 2/3 and then "SUCCESS: 3/3 tokens collected".
4. Further input does not change the completed state.
5. Log engine version, exact action sequence, expected and actual display, screenshot or video and pass/fail.

**Evaluation dimensions:** reproduction clarity, root-cause diagnosis, functional correctness, feature completeness, reproducibility, communication.

**Scope limitation:** one-room demonstrator; no physics, art assets, automated integration tests, performance claims or shipped title credits.