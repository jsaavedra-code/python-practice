# 🧠 Basic NPC Detector

A simple (and slightly judgmental) Python program that tries to determine whether you're an **NPC** or a **main character** in your own life.

This is not psychology.
This is not science.
This is vibes, logic, and a bit of pattern recognition.

---

## 🚀 What it does

The program asks you:

* 5 **yes/no questions** (basic self-awareness checks)
* 5 **open-ended questions** (this is where it gets interesting)

Then it analyzes your answers using:

* keyword patterns
* basic reasoning signals
* detection of generic vs thoughtful responses

Finally, it classifies you as:

* 🧍 **Main Character**
* 😐 **Mid**
* 🤖 **NPC (womp womp)**

---

## 🧩 How it works (quick logic)

Each open answer is evaluated like this:

* Looks for **"main character" signals**
  (e.g. *"because"*, *"I think"*, *"for me"*, *"I realized"*)

* Looks for **"NPC signals"**
  (e.g. *"idk"*, *"whatever"*, *"not much"*, *"stuff"*)

Then:

* strong main signal → `+1`
* strong npc signal → `-1`
* unclear → `0`

Yes/no questions also contribute to the score.

---

## 📊 Scoring

Final score range:

* Minimum: **-5**
* Maximum: **10**

Results:

* `>= 8` → 🧠 **Main Character**
* `>= 4` → 😐 **Mid**
* `< 4` → 🤖 **NPC detected**

---

## ⚠️ Disclaimer

This is a **fun heuristic**, not a real personality test.

You can absolutely:

* game it
* trick it
* or fail it while being a genius

That said…
most NPCs won’t notice how to game it.

---

## ▶️ How to run

Make sure you have Python installed.

```bash
python npc_detector.py
```

Then just answer the questions.

---

## 🧪 Example vibe

**NPC answer:**

> idk just chilling, the usual

**Main character answer:**

> I usually read or build things because I like understanding how systems work

---

## 🛠️ Future ideas

* detect answer length / effort
* penalize vague answers harder
* detect "fake deep" responses
* improve phrase weighting

---

## 🧠 Why this exists

Because most people:

* don’t question their behavior
* don’t reflect
* and answer everything with templates

This tries (very roughly) to detect that.

---

## 👤 Author

Built by someone who:

* overthinks everything
* questions patterns
* and got bored

---

## ⭐ If you found it interesting

Give it a star or improve it.

Or don’t.
That would also be… very NPC-like.

- John Saavedra