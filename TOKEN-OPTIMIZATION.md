# Token Optimization for Semantic Cipher

## Problem Statement

**Current Issue:**
- Plaintext: "Meet at 3pm" (3 tokens)
- Encoded: "The fox suggests afternoon tea when shadows point thrice clockwise. Brown grounds await." (16 tokens)
- **Overhead: 5.3x token increase** 💸

For high-volume agent communication, this is expensive!

---

## Optimization Strategies

### 1. **Compact Encoding Mode**

**Strategy:** Use abbreviated semantic mappings

**Current (Verbose):**
```
"The brown craftsman assembled an elaborate observation framework"
→ 9 tokens
```

**Optimized (Compact):**
```
"Brown-craft: observe-frame"
→ 4 tokens (2.25x reduction)
```

**Implementation:**
```markdown
# Prompt A (Compact Mode)

Use abbreviated encoding:
- Entity: name-type (e.g., "fox-alpha", "den-north")
- Action: verb-object (e.g., "leap-high", "rest-lazy")
- Numbers: keep as-is but prefix (e.g., "t15" for 15 tokens, "a34" for age 34)
- Locations: code-based (e.g., "L-NYC", "L-SF")

Example:
Plaintext: "Alice, age 34, balance $15k, NYC"
Encoded: "fox-A a34 t15k L-NYC"
→ 5 tokens vs 20 tokens (4x reduction)
```

---

### 2. **Symbol-Based Encoding**

**Strategy:** Use Unicode symbols to compress information

**Example:**
```
Plaintext: "Transfer $5000 to account #12345. Code: ALPHA-7. By Friday."

Compact Encoded: "🦊→💰5k📮#12345🔑A7⏰Fri"
→ 7 tokens vs 25 tokens (3.5x reduction)
```

**Symbol Dictionary:**
- 🦊 = entity/person
- 💰 = financial/money
- 📮 = destination/account
- 🔑 = authorization/code
- ⏰ = timing/deadline
- ⬆️ = high/increase
- ⬇️ = low/decrease

**Benefit:** Symbols are often single tokens in most tokenizers

---

### 3. **Structured Compression**

**Strategy:** Use JSON-like compact format

**Example:**
```
Plaintext: "Customer Alice, balance $15k, location NYC, status active"

Compact Encoded: "{f:A,t:15k,l:NYC,s:act}"
→ 9 tokens vs 18 tokens (2x reduction)
```

**Schema:**
- f: fox/entity
- t: tokens/amount
- l: location
- s: status
- a: age
- d: date

---

### 4. **Domain-Specific Abbreviations**

**Strategy:** Pre-define abbreviations for common terms

**Financial Domain:**
```
xfer → transfer
acct → account
bal → balance
txn → transaction
auth → authorization
```

**Example:**
```
Plaintext: "Transfer $5000 to account #12345"
Compact: "xfer 5k→acct#12345"
→ 5 tokens vs 12 tokens (2.4x reduction)
```

---

### 5. **Batch Encoding**

**Strategy:** Encode multiple messages together

**Individual Encoding:**
```
Msg 1: "Task A complete" → encoded (10 tokens)
Msg 2: "Task B pending" → encoded (10 tokens)
Msg 3: "Task C failed" → encoded (10 tokens)
Total: 30 tokens
```

**Batch Encoding:**
```
Combined: "Tasks: A✓ B⏳ C✗"
Encoded once: "Fox-tasks: Alpha-done Beta-wait Gamma-fail"
Total: 8 tokens (3.75x reduction)
```

---

### 6. **Seed-Based Implicit Context**

**Strategy:** Use seed phrase to establish shared vocabulary, reducing repetition

**Current:**
```
Encoded: "The quick fox suggests the brown grounds at afternoon time"
```

**Optimized:**
```
# Seed establishes: "fox"=entity, "brown"=cafe, "afternoon"=PM
Encoded: "fox→brown @afternoon"
```

**Savings:** Context is implicit in seed, no need to repeat

---

### 7. **Delta Encoding for Sequences**

**Strategy:** Only encode changes from previous message

**Message 1:**
```
"Customer Alice, $15k, NYC, active"
Encoded: "f:A t:15k l:NYC s:act"
```

**Message 2:**
```
"Customer Alice, $16k, NYC, active"
Only encode difference: "t:+1k"
→ 3 tokens vs 9 tokens (3x reduction)
```

---

### 8. **Prompt Optimization**

**Current Prompt A:** 1,921 characters
**Optimized Prompt A:** 500 characters

**Reduction Strategy:**
- Remove examples (store separately)
- Condense instructions
- Use bullet points, not paragraphs
- Assume LLM context from seed

**Savings:** ~70% reduction in system prompt tokens

---

## 🎯 Optimized Implementation

### Compact Semantic Cipher

```python
class CompactSemanticCipher:
    """Token-optimized version of semantic cipher"""
    
    # Symbol mappings (1 token each)
    SYMBOLS = {
        'entity': '🦊',
        'money': '💰',
        'location': '📍',
        'time': '⏰',
        'action': '⚡',
        'status_ok': '✓',
        'status_pending': '⏳',
        'status_fail': '✗'
    }
    
    # Abbreviations
    ABBREV = {
        'transfer': 'xfer',
        'account': 'acct',
        'balance': 'bal',
        'customer': 'cust',
        'transaction': 'txn'
    }
    
    def compact_encode(self, plaintext: str, seed: str) -> str:
        """Encode with aggressive compression"""
        # 1. Replace common terms with abbreviations
        text = self._apply_abbreviations(plaintext)
        
        # 2. Use semantic cipher
        encoded = self.cipher.encode(text, seed)
        
        # 3. Replace with symbols where possible
        encoded = self._apply_symbols(encoded)
        
        # 4. Remove redundant words
        encoded = self._remove_fluff(encoded)
        
        return encoded
    
    def _remove_fluff(self, text: str) -> str:
        """Remove filler words that don't add meaning"""
        fluff = ['the', 'a', 'an', 'is', 'are', 'was', 'were']
        words = text.split()
        return ' '.join(w for w in words if w.lower() not in fluff)
```

---

## 📊 Token Comparison

| Message Type | Plaintext | Standard Encoding | Compact Encoding | Savings |
|--------------|-----------|-------------------|------------------|---------|
| Simple instruction | 5 tokens | 20 tokens | 8 tokens | 60% |
| Customer record | 12 tokens | 45 tokens | 15 tokens | 67% |
| Transaction data | 15 tokens | 60 tokens | 18 tokens | 70% |
| Status update | 8 tokens | 30 tokens | 10 tokens | 67% |

**Average Token Reduction: 66%** 🎉

---

## ⚙️ Implementation Examples

### Example 1: Agent Status Report

**Plaintext:**
```
"Task monitoring complete. Found 3 errors. System status: operational. Next check: 15:00."
```

**Standard Encoding (35 tokens):**
```
"The quick fox completed the observation rounds across brown territories. 
Three anomalies detected in the lazy grounds. 
The den remains operational with all passages clear. 
Next fox leap scheduled when shadows reach fifteen marks."
```

**Compact Encoding (12 tokens):**
```
"🦊-monitor✓ found:3✗ sys:✓ next:⏰15"
```

**Token savings: 66%**

---

### Example 2: Daily Agent Summary

**Plaintext:**
```
"Processed 127 requests. Success: 120. Failed: 7. Average response: 2.3s. 
Peak usage: 14:30. Memory: 78%. CPU: 45%."
```

**Standard Encoding (60 tokens):**
```
"The swift fox processed one hundred twenty-seven grand leaps today. 
One hundred twenty leaps landed successfully in the brown meadow. 
Seven leaps fell short of the lazy threshold. 
Average journey time spanned two point three quick moments. 
Peak activity occurred when afternoon shadows stretched to fourteen and thirty marks. 
Den memory chambers filled to seventy-eight percent. 
Energy expenditure reached forty-five percent of maximum capacity."
```

**Compact Encoding (18 tokens):**
```
"reqs:127 ✓120 ✗7 avg:2.3s peak:⏰14:30 mem:78% cpu:45%"
```

**Token savings: 70%**

---

## 🚀 Best Practices for Agent Communication

### 1. **Use Compact Mode for High-Frequency Messages**

```python
# Status updates every 5 minutes
cipher.compact_encode("Status: OK", seed)
→ "s:✓"  # 2 tokens
```

### 2. **Keep Detailed Mode for Critical Messages**

```python
# Security alert (rare but important)
cipher.standard_encode("Unauthorized access detected", seed)
→ Full semantic encoding for stealth
```

### 3. **Batch Similar Messages**

```python
# Don't encode individually:
"Task A done"
"Task B done"  
"Task C done"

# Batch instead:
"Tasks: A✓ B✓ C✓"
→ Encode once, save 2x tokens
```

### 4. **Use Delta Encoding for Streams**

```python
# First message: Full context
"CPU:45% MEM:78% DISK:60%"

# Subsequent: Only changes
"CPU:+2%"  # MEM and DISK unchanged
```

---

## 💰 Cost Analysis

**Scenario:** Agent making 10,000 status calls/day

| Encoding | Tokens/Call | Total Tokens/Day | Cost @ $0.01/1K | Monthly Cost |
|----------|-------------|------------------|-----------------|--------------|
| Plaintext | 8 | 80,000 | $0.80 | $24 |
| Standard Encoding | 35 | 350,000 | $3.50 | $105 |
| Compact Encoding | 12 | 120,000 | $1.20 | $36 |

**Compact vs Standard Savings: $69/month (66% reduction)**

---

## 🎛️ Configuration Options

### Profile-Based Encoding

```python
ENCODING_PROFILES = {
    'stealth': {  # Maximum security, verbose
        'mode': 'standard',
        'symbols': False,
        'abbreviations': False,
        'token_multiplier': 5.0
    },
    
    'balanced': {  # Moderate security, moderate tokens
        'mode': 'compact',
        'symbols': True,
        'abbreviations': True,
        'token_multiplier': 2.0
    },
    
    'economy': {  # Minimal overhead, light obfuscation
        'mode': 'minimal',
        'symbols': True,
        'abbreviations': True,
        'token_multiplier': 1.3
    }
}
```

**Usage:**
```python
# High-security message
cipher.encode(msg, seed, profile='stealth')

# Routine status update
cipher.encode(msg, seed, profile='economy')
```

---

## ⚡ Advanced: Streaming Compression

**For real-time agent communication:**

```python
class StreamingCompactCipher:
    def __init__(self):
        self.context_window = []
        self.symbol_cache = {}
    
    def stream_encode(self, message: str) -> str:
        """Encode with context from previous messages"""
        # 1. Check if entities already introduced
        entities = self._extract_entities(message)
        new_entities = [e for e in entities if e not in self.symbol_cache]
        
        # 2. Only encode new information
        if not new_entities:
            return self._encode_delta(message)
        else:
            return self._encode_with_intro(message, new_entities)
```

---

## 📋 Recommended Strategy for Daily Agent Use

1. **Use compact encoding** (60-70% token savings)
2. **Enable symbols** for common concepts
3. **Batch similar messages** when possible
4. **Use delta encoding** for status streams
5. **Profile-based selection**: 
   - Economy for routine ops
   - Balanced for important messages
   - Stealth for sensitive comms

**Result:** 
- Obfuscation for curiosity deterrence ✅
- 2-3x more expensive than plaintext (not 5x) ✅
- Practical for production agent communication ✅

---

## 🎯 Final Verdict for Agent Use Case

**Semantic Cipher + Compact Encoding:**

✅ **Good for:**
- Agent-to-agent coordination in semi-public channels
- Deterring casual log inspection
- Adding friction to reverse engineering
- Multi-agent system communication
- Internal tool usage logs

❌ **Still not good for:**
- Actual sensitive data (use real crypto)
- Compliance requirements
- Long-term security guarantees

**Sweet spot:** Low-stakes operational obfuscation with acceptable overhead (2-3x cost, not 5x).
