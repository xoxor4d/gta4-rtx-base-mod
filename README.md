## Base Remix-Mod for the GTAIV RTX Remix Compatibility Mod

This is an actual __remix__ mod for GTAIV. It is meant as a base for the [GTAIV RTX Remix Compatibility Mod](https://github.com/xoxor4d/gta4-rtx).  

<br>

It handles: 
- Ships a few PBR materials like:
  - Broker Safehouse
  - Generic Road Textures
  - Some NPC textures
- Makes water look like water
- Makes a lot of glass translucent
- Various mesh fixes

<br>

### Installation

Use the installer that comes with the Compatibility Mod _OR_ install manually:
- [Download repo as zip](https://github.com/xoxor4d/gta4-rtx-base-mod/archive/refs/heads/master.zip)
- Place the `mods` folder into the `rtx-remix` folder found in the GTAIV root folder  
(see Folder Structure below)

<br>

<div align="center" markdown="1">

<h2>Folder Structure</h3>
<a name=""></a>
</div>

```
.  
├─ ...
├─ 📁 steamapps
│  └─📁 common
│     └─📁 Grand Theft Auto IV
│       └─📁 GTAIV
│         ├── 📜 GTAIV.exe.exe
│         ├── 📜 d3d9.dll
│         ├── 📜 ...
│         │
│         ├── 📁 .trex
│         │   ├── 📜 d3d9.dll
│         │   ├── 📜 NvRemixBridge.exe
│         │   └── ...
│         │
│         ├── 📁 rtx_comp
│         └── 📁 rtx-remix
│             └─📁 mods
│               └─📁 gta4rtx
│                 ├── 📜 comp_cars.usda
│                 ├── 📜 comp_effects.usda
│                 ├── 📜 mod.usda
│                 └── ...
└── ...  
```