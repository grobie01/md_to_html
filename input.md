# Building a Custom Mechanical Keyboard

[TOC]

## Introduction

Building your own mechanical keyboard can be a rewarding project that results in a perfectly customized typing experience. This guide will walk you through the basic components and assembly process.

## Components Needed

The following components are essential for any custom mechanical keyboard build:

* PCB (Printed Circuit Board)
* Switches
* Keycaps
* Case
* Stabilizers
* USB-C Cable

## Switch Options

There are three main categories of mechanical switches:

| Type | Characteristics | Actuation Force | Common Use |
|------|----------------|-----------------|------------|
| Linear | Smooth keypress without tactile bump | 45g-60g | Gaming |
| Tactile | Noticeable bump during keypress | 55g-65g | General typing |
| Clicky | Tactile bump with audible click | 50g-70g | Typing, but loud |

## Assembly Steps

### 1. Prepare the PCB

First, test your PCB by connecting it to your computer and using a metal tool to bridge the switch connections. You can use a tool like VIA to verify each switch position works:

```bash
# Install VIA on Ubuntu/Debian
sudo apt update
sudo apt install via-keyboard
```

### 2. Install Stabilizers

Stabilizers are crucial for larger keys like the spacebar. Here's how to tune them:

```python
def lube_stabilizer(stab):
    """
    Apply lubricant to stabilizer
    """
    components = ['wire', 'housing', 'stem']
    for part in components:
        apply_205g0(stab[part])
    return stab
```

### 3. Mount Switches

When mounting switches, ensure they're fully seated in the plate and PCB. The pins should be straight and insert smoothly into the PCB holes.

## Programming the Firmware

Most custom keyboards use QMK firmware. Here's a sample keymap:

```c
const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT(
        KC_ESC,  KC_1,    KC_2,    KC_3,    KC_4,    KC_5,    
        KC_TAB,  KC_Q,    KC_W,    KC_E,    KC_R,    KC_T
    )
};
```

## Maintenance Tips

Regular maintenance will extend the life of your keyboard:

1. Clean keycaps monthly with warm water and mild soap
2. Use compressed air to remove dust
3. Re-lubricate switches every 6-12 months depending on usage

## Resources

For more information, check out:
* [QMK Documentation](https://docs.qmk.fm/)
* [Keyboard University](https://keyboard.university/)
* [r/mechanicalkeyboards](https://reddit.com/r/mechanicalkeyboards)

## Conclusion

Building a custom keyboard takes time and patience, but the result is a unique input device tailored exactly to your preferences. Take your time with each step, and don't hesitate to ask the community for help when needed.