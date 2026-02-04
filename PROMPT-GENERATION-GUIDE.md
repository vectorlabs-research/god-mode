# How to Generate Prompt A and Prompt B

## Overview

Prompt A (Encoding) and Prompt B (Decoding) are the "keys" to the semantic cipher. They must be carefully designed to work together while resisting unauthorized decoding.

---

## Design Principles

### 1. Complementary Design
- **Prompt A** defines the encoding strategy
- **Prompt B** must understand and reverse that strategy
- They are semantic inverses of each other

### 2. Seed Phrase Integration
- Both prompts use the seed phrase as a contextual anchor
- The seed creates consistent semantic mappings
- Same seed + same plaintext should produce similar (but not identical) encodings

### 3. Security Through Obscurity
- Without the prompts, the seed phrase alone is useless
- The semantic mapping strategy is the actual "key"
- Multiple valid encoding strategies can exist

---

## Prompt A (Encoding) Components

### Required Elements:

1. **Role Definition**
   ```
   You are a semantic encoder.
   ```

2. **Task Description**
   ```
   Transform plaintext into semantically encoded messages using a seed phrase.
   ```

3. **Encoding Rules**
   - What to preserve (numbers, specifics)
   - What to obscure (keywords, structure)
   - What to create (natural-sounding output)

4. **Semantic Mapping Strategy**
   - How to use the seed phrase
   - How to create metaphors
   - How to embed information

5. **Example**
   - Concrete demonstration of encoding
   - Shows the desired output style

6. **Output Format**
   - Plain text only, no metadata

### Example Prompt A Structure:

```markdown
# Prompt A - Encoding

## Role
You are a semantic encoder...

## Instructions
Given plaintext and seed phrase, transform message by:
- Mapping plaintext concepts to seed phrase concepts
- Using metaphorical language
- Creating natural-sounding output

## Rules
- DO: Preserve numbers accurately
- DON'T: Use obvious substitutions
- DO: Sound natural and innocent

## Example
Plaintext: "Meet at 3pm"
Seed: "The quick brown fox"
Encoded: "The fox suggests afternoon tea at thrice o'clock"

## Output
Return ONLY the encoded message.
```

---

## Prompt B (Decoding) Components

### Required Elements:

1. **Role Definition**
   ```
   You are a semantic decoder.
   ```

2. **Task Description**
   ```
   Recover original plaintext from encoded messages using seed phrase.
   ```

3. **Decoding Rules**
   - How to identify semantic mappings
   - How to reverse metaphors
   - How to extract precise information

4. **Decoding Strategy**
   - Parse for seed phrase references
   - Identify metaphorical constructs
   - Reconstruct original meaning

5. **Example**
   - Same example as Prompt A, but reversed
   - Shows the decoding process

6. **Output Format**
   - Plain text only, exact original message

7. **Failure Handling**
   - What to return if decoding fails
   - `[DECODE_FAILED]` convention

### Example Prompt B Structure:

```markdown
# Prompt B - Decoding

## Role
You are a semantic decoder...

## Instructions
Given encoded message and seed phrase, recover the original by:
- Identifying seed phrase references
- Reversing metaphorical transformations
- Extracting exact information

## Rules
- Numbers must be exact
- Timing must be precise
- Codes must be preserved

## Example
Encoded: "The fox suggests afternoon tea at thrice o'clock"
Seed: "The quick brown fox"
Decoded: "Meet at 3pm"

## Output
Return ONLY the decoded plaintext.
If failed: [DECODE_FAILED]
```

---

## Generation Process

### Step 1: Define Your Encoding Strategy

Choose a strategy, e.g.:
- **Animal mapping:** Use seed animals as metaphors
- **Time transformation:** Encode times poetically
- **Location obfuscation:** Use seed concepts for places

Example: "The quick brown fox jumps over the lazy dog"
- fox = actor/person
- brown = cafe/coffee
- quick = urgent/fast
- lazy = relaxed/end of day
- jumps = action/movement
- dog = passive/stationary

### Step 2: Create Consistent Mappings

Document how concepts map:
```
Meeting → fox suggests
Time 3pm → thrice o'clock / afternoon three
Place (cafe) → brown grounds
Action (transfer) → fox leaps
Urgency → quick
Completion → lazy day ends
```

### Step 3: Write Prompt A

Include:
- Clear role and task
- Your encoding strategy
- Specific rules (preserve numbers, etc.)
- 2-3 examples
- Output format instructions

### Step 4: Write Prompt B

Mirror Prompt A but reversed:
- Same examples, decoded
- Reversal of encoding strategy
- Failure handling

### Step 5: Test Together

1. Encode a test message with Prompt A
2. Decode with Prompt B
3. Verify accuracy
4. Iterate until stable

### Step 6: Test Security

1. Try to decode without Prompt B
2. Try with wrong seed phrase
3. Try with partial prompts
4. Verify all fail appropriately

---

## Advanced Techniques

### 1. Layered Encoding

Add multiple semantic layers:
```
Layer 1: Seed phrase mapping
Layer 2: Contextual embedding
Layer 3: Stylistic transformation
```

### 2. Domain-Specific Prompts

Create prompts for specific domains:
- Financial transactions
- Military commands
- Medical communications
- Social coordination

### 3. Versioning

Maintain multiple prompt versions:
- A1/B1: General purpose
- A2/B2: High security
- A3/B3: Speed optimized

### 4. Multi-Agent Encoding

Chain multiple encode/decode cycles:
```
Plaintext → [A1+S1] → Encoded1 → [A2+S2] → Encoded2
Encoded2 → [B2+S2] → Decoded1 → [B1+S1] → Plaintext
```

---

## Best Practices

### DO:
✅ Test extensively with real messages
✅ Use concrete examples in prompts
✅ Specify output format clearly
✅ Handle edge cases (numbers, codes)
✅ Version your prompts

### DON'T:
❌ Make prompts too complex
❌ Use obvious substitution rules
❌ Forget failure handling
❌ Skip security testing
❌ Leak prompt details publicly

---

## Prompt Templates

See `prompts/` directory for:
- `PROMPT-A-ENCODE.md` - Current production encoding prompt
- `PROMPT-B-DECODE.md` - Current production decoding prompt
- `PROMPT-A-V2-TEMPLATE.md` - Template for creating variants
- `PROMPT-B-V2-TEMPLATE.md` - Template for creating variants

---

## Testing Your Prompts

Use `test_engine.py`:

```python
cipher = SemanticCipher()
plaintext = "Your test message"
seed = "Your seed phrase"

# Test encode
encoded = cipher.encode(plaintext, seed)

# Test decode
decoded = cipher.decode(encoded, seed)

# Verify
assert plaintext == decoded
```

Run stability tests:
```bash
python test_stability.py --rounds 10 --messages test_messages.txt
```

---

## Security Considerations

1. **Prompt Secrecy:** Prompts A and B must remain secret
2. **Seed Publication:** Seed phrase can be public (adds plausible deniability)
3. **Pattern Resistance:** Vary encodings to prevent pattern recognition
4. **Failure Modes:** Ensure wrong seed/prompt produces garbage, not partial success

---

## Conclusion

Generating effective Prompt A and Prompt B requires:
1. Clear semantic mapping strategy
2. Careful testing and iteration
3. Security validation
4. Documentation of the approach

The current prompts in this repository have been tested and validated. Use them as templates for creating your own variants.
