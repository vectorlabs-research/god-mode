#!/usr/bin/env python3
"""
Semantic Cipher Engine

A novel encryption approach using LLM semantics to encode/decode messages
with a public seed phrase and secret semantic prompts.
"""

import os
import json
from pathlib import Path
from typing import Optional

# For LLM calls - assuming OpenAI-compatible API
try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False
    print("Warning: openai package not installed. Install with: pip install openai")


class SemanticCipher:
    """Semantic cipher engine for encoding/decoding messages."""
    
    def __init__(self, 
                 model: str = "anthropic/claude-sonnet-4",
                 api_base: Optional[str] = None,
                 api_key: Optional[str] = None):
        """
        Initialize the semantic cipher engine.
        
        Args:
            model: LLM model to use for encoding/decoding
            api_base: API base URL (defaults to OpenRouter)
            api_key: API key (defaults to env OPENROUTER_API_KEY)
        """
        if not HAS_OPENAI:
            raise ImportError("openai package required. Install with: pip install openai")
        
        self.model = model
        self.api_base = api_base or "https://openrouter.ai/api/v1"
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        
        if not self.api_key:
            raise ValueError("API key required. Set OPENROUTER_API_KEY env var or pass api_key parameter")
        
        self.client = OpenAI(
            base_url=self.api_base,
            api_key=self.api_key
        )
        
        # Load prompts
        prompts_dir = Path(__file__).parent / "prompts"
        self.prompt_a = (prompts_dir / "PROMPT-A-ENCODE.md").read_text()
        self.prompt_b = (prompts_dir / "PROMPT-B-DECODE.md").read_text()
    
    def encode(self, plaintext: str, seed_phrase: str) -> str:
        """
        Encode a plaintext message using the seed phrase.
        
        Args:
            plaintext: Original message to encode
            seed_phrase: Public seed phrase for semantic mapping
            
        Returns:
            Encoded message that looks like natural language
        """
        if not plaintext or not plaintext.strip():
            raise ValueError("Plaintext cannot be empty")
        
        if not seed_phrase or not seed_phrase.strip():
            raise ValueError("Seed phrase cannot be empty")
        
        user_message = f"""Seed Phrase: "{seed_phrase}"

Plaintext to encode: "{plaintext}"

Encode this message."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.prompt_a},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,  # Some creativity for natural language
            max_tokens=1000
        )
        
        encoded = response.choices[0].message.content.strip()
        return encoded
    
    def decode(self, encoded_message: str, seed_phrase: str) -> str:
        """
        Decode a semantically encoded message using the seed phrase.
        
        Args:
            encoded_message: Semantically encoded message
            seed_phrase: Public seed phrase used during encoding
            
        Returns:
            Original plaintext message
        """
        if not encoded_message or not encoded_message.strip():
            raise ValueError("Encoded message cannot be empty")
        
        if not seed_phrase or not seed_phrase.strip():
            raise ValueError("Seed phrase cannot be empty")
        
        user_message = f"""Seed Phrase: "{seed_phrase}"

Encoded message: "{encoded_message}"

Decode this message."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.prompt_b},
                {"role": "user", "content": user_message}
            ],
            temperature=0.0,  # Deterministic decoding
            max_tokens=1000
        )
        
        decoded = response.choices[0].message.content.strip()
        
        # Check for decode failure
        if decoded == "[DECODE_FAILED]":
            raise ValueError("Decoding failed - wrong seed or corrupted message")
        
        return decoded


def main():
    """CLI interface for testing."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Semantic Cipher Engine")
    parser.add_argument("action", choices=["encode", "decode"], help="Action to perform")
    parser.add_argument("--message", "-m", required=True, help="Message to encode/decode")
    parser.add_argument("--seed", "-s", required=True, help="Seed phrase")
    parser.add_argument("--model", default="anthropic/claude-sonnet-4", help="LLM model to use")
    
    args = parser.parse_args()
    
    cipher = SemanticCipher(model=args.model)
    
    if args.action == "encode":
        result = cipher.encode(args.message, args.seed)
        print(f"\n📤 ENCODED MESSAGE:")
        print(result)
    else:
        result = cipher.decode(args.message, args.seed)
        print(f"\n📥 DECODED MESSAGE:")
        print(result)


if __name__ == "__main__":
    main()
