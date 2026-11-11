# FINDME — The Forgotten Administrator

An administrator once maintained this machine.

Before disappearing, they left behind traces of an old authentication mechanism.

The machine is still operational, but access to its internal system is restricted.

Your objective is simple:

**Find the forgotten password and authenticate yourself.**

Some files may be hidden.  
Some files may not be what they appear to be.  
Some information may require reconstruction.

The filesystem contains everything you need.

Good luck.

---

## Requirements.

- Linux environment
- Python 3
- Standard Linux utilities: `xxd`, `bzip2`, `gzip`, and `tar`

## Running the Challenge

Extract the downloaded archive:

```bash
tar -xzf findme.tar.gz
```

Enter the challenge directory:

```bash
cd findme
```

Launch the recovery environment:

```bash
./challenge/run
```

Follow the clues throughout the filesystem to recover the forgotten administrator password.

**Note:** This challenge is intended to be completed locally on a Linux system.