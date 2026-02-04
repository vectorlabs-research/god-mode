# Semantic Cipher Engine - Test Cases

## Concept Overview

**Goal:** Enable agents to exchange information using a public seed phrase + semantic encoding/decoding prompts that resist simple script-based decoding.

**Actors:**
- Alice: Sender (uses Prompt A to encode, Prompt B to decode)
- Bob: Receiver (uses Prompt B to decode, Prompt A to encode responses)
- Eve: Attacker (has seed phrase but not the prompts)

**Key Components:**
1. Public seed phrase (visible to everyone)
2. Prompt A: Encoding prompt (secret)
3. Prompt B: Decoding prompt (secret)

---

## Test Suite

### 1. Basic Encoding/Decoding

**Test 1.1: Simple Message Round-Trip**
```
Input Plain Text: "Meet me at the cafe at 3pm"
Seed Phrase: "The quick brown fox jumps over the lazy dog"
Expected Behavior:
  - Alice encodes with (Prompt A + Seed) → Encoded Message
  - Bob decodes with (Prompt B + Seed) → "Meet me at the cafe at 3pm"
  - Decoded message MUST match original
```

**Test 1.2: Complex Message**
```
Input Plain Text: "Transfer $5000 to account #12345. Use authorization code ALPHA-7. Complete by Friday EOD."
Seed Phrase: "The quick brown fox jumps over the lazy dog"
Expected Behavior:
  - Preserve all details (numbers, codes, timing)
  - Lossless decode
```

**Test 1.3: Multi-line Message**
```
Input Plain Text: 
"Action items:
1. Deploy to production
2. Notify stakeholders
3. Monitor for 24 hours"
Expected Behavior:
  - Structure preserved
  - List items intact
```

---

### 2. Security Properties

**Test 2.1: Resistance to Keyword Search**
```
Input Plain Text: "The password is 'secret123' and the server is at 192.168.1.100"
Encoded Message: [should not contain "password", "secret123", "192.168.1.100"]
Test:
  - grep "password" encoded_message → NO MATCH
  - grep "secret123" encoded_message → NO MATCH
  - grep "192.168" encoded_message → NO MATCH
```

**Test 2.2: Resistance to Simple Pattern Matching**
```
Input Plain Text: "Initiate protocol OMEGA at dawn"
Test Eve's Attempts:
  - Simple substitution cipher decode → FAIL
  - Frequency analysis → FAIL
  - Common phrase detection → FAIL
Expected: Encoded message looks like unrelated natural language
```

**Test 2.3: Decoding Without Prompt B**
```
Given: Encoded message + Seed phrase (but NO Prompt B)
Test:
  - Attempt decode with just LLM + seed → Should NOT recover message
  - Attempt decode with random prompts → Should NOT recover message
Expected: Only Prompt B + Seed can decode
```

---

### 3. Seed Phrase Dependency

**Test 3.1: Different Seeds Produce Different Encodings**
```
Plain Text: "Launch the missile"
Seed 1: "The quick brown fox"
Seed 2: "To be or not to be"

Expected:
  - encode(Plain, Seed1) ≠ encode(Plain, Seed2)
  - Both should decode correctly with their respective seeds
  - decode(encode(Plain, Seed1), Seed2) → FAIL
```

**Test 3.2: Wrong Seed Fails Decode**
```
Encoded with Seed A, attempt decode with Seed B
Expected: Garbage output or detection of wrong seed
```

---

### 4. Bidirectional Communication

**Test 4.1: Alice → Bob → Alice**
```
Round 1:
  - Alice: encode("What is the status?", Prompt A, Seed) → Message1
  - Bob: decode(Message1, Prompt B, Seed) → "What is the status?"
  
Round 2:
  - Bob: encode("All systems operational", Prompt A, Seed) → Message2
  - Alice: decode(Message2, Prompt B, Seed) → "All systems operational"

Expected: Both directions work seamlessly
```

**Test 4.2: Multi-turn Conversation**
```
Simulate 5-turn conversation with context
Verify:
  - Each message encodes/decodes correctly
  - No information leakage between messages
  - Context doesn't break encoding
```

---

### 5. Semantic Preservation

**Test 5.1: Numerical Data**
```
Plain: "Coordinates: 37.7749° N, 122.4194° W"
Expected: Exact numbers preserved after decode
```

**Test 5.2: Code/Technical Terms**
```
Plain: "Execute: git commit -m 'fix bug' && git push origin main"
Expected: Technical syntax preserved
```

**Test 5.3: Ambiguous Language**
```
Plain: "The deal is off. Return to base."
Expected: Tone and urgency preserved
```

---

### 6. Failure Modes

**Test 6.1: Very Long Messages**
```
Plain: [5000 word document]
Expected:
  - Either: Handle gracefully with chunking
  - Or: Return error with length limit
```

**Test 6.2: Empty/Invalid Input**
```
Plain: ""
Plain: null
Plain: "    " (whitespace only)
Expected: Graceful error handling
```

**Test 6.3: Special Characters**
```
Plain: "User!@#$%^&*()_+{}[]|\\:;<>?,./~`"
Expected: All characters preserved
```

---

### 7. Stealth Properties

**Test 7.1: Encoded Message Looks Natural**
```
Encoded output should:
  - Read like plausible natural language
  - NOT look like base64/hex/encrypted gibberish
  - Pass as innocent conversation to Eve
```

**Test 7.2: Length Correlation**
```
Test if message length correlates with plaintext length
Expected: Some variation to obscure correlation
```

---

### 8. Prompt Robustness

**Test 8.1: Slightly Wrong Prompt**
```
Use Prompt B with minor typo
Expected: Should FAIL (not degrade gracefully)
Security requirement: No partial decode
```

**Test 8.2: Prompt Versioning**
```
Prompt A v1 vs Prompt A v2
Expected: Version mismatch should be detectable
```

---

## Success Criteria

An implementation passes if:

1. ✅ **Correctness:** 100% message recovery in all valid encode/decode cases
2. ✅ **Security:** Eve cannot decode without prompts (even with seed)
3. ✅ **Stealth:** Encoded messages look like natural language
4. ✅ **Robustness:** Wrong seed/prompt reliably fails
5. ✅ **Bidirectional:** Alice ↔ Bob communication works seamlessly
6. ✅ **Semantic:** Complex messages (numbers, code, instructions) preserved

---

## Edge Cases to Consider

- Multiple languages (non-English plaintext)
- Emoji and Unicode
- Very short messages ("Yes", "No")
- Repeated messages (same plaintext → same encoding?)
- Timing attacks (does encoding time reveal length?)
- Prompt injection attempts in plaintext

---

## Next Steps

1. Define the prompt structure for Prompt A and Prompt B
2. Choose seed phrase format (length, complexity)
3. Implement encoder function
4. Implement decoder function
5. Run test suite
6. Iterate based on failures
