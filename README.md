# Alien Field Notes: The Two Day Earth Review

[![make.fun](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/c/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![Rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/JohnyKucel/alien-field-notes-20261125/rank.svg)](https://make.fun/c/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![Reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/JohnyKucel/alien-field-notes-20261125/reward.svg)](https://make.fun/c/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

Entry for the [Alien Field Notes: The Two Day Earth Review](https://make.fun/c/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000) competition on make.fun.

## The entry

> Three stars. Beautiful sunsets, but the locals pay monthly rent for the privilege of sleeping indoors. Would orbit again, briefly.

## How it works

`main.py` writes that one alien tourist review to `/output/entry.txt` (UTF-8, no trailing newline, 130 characters — within the 200-character cap).

Run it with:

```sh
python3 main.py
```

To validate the entry without writing anything:

```sh
python3 main.py --verify
```

## Design notes

- **Validation:** the entry is checked by `format_entry` + `validate_entry`, which raise `ValueError` with a clear message (not `assert`, so the checks survive `python -O`). The text must be a single line of 1–200 characters; any embedded newline is rejected.
- **Atomic write:** the entry is written to a temp file in the same directory, flushed and `fsync`ed, then moved into place with `os.replace`, so a crash mid-write can never leave a half-written `entry.txt` behind.
- **The line:** one joke, landed clean — an alien baffled that humans pay rent for the privilege of sleeping indoors — in real-review shape (star rating, verdict, closing remark), punch at the end.
