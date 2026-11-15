# Shelf sources and licence evidence

Every title in `catalog.json` was checked against the licence file in its own
repository (not the itch.io page or a README claim) on 2026-11-14. The rule:
the licence text, or a written statement by the author, must permit
redistribution of the compiled ROM; NonCommercial and NoDerivs terms do not
qualify; nothing with Nintendo or other third-party characters, names or
assets; no ROM hacks. Where no stable author-hosted file exists, the ROM is
mirrored under `roms/` with its licence text beside it in `LICENSES/`.

## Listed

| id | Title | System | Licence (verified file) | ROM source used | Evidence |
|---|---|---|---|---|---|
| tobu-tobu-girl-deluxe | Tobu Tobu Girl Deluxe | GBC | MIT (code), CC BY 4.0 (all assets) | mirror `roms/tobu-tobu-girl-deluxe.gb` (itch has no stable URL; same file Tinbox bundles) | [LICENSE](https://raw.githubusercontent.com/SimonLarsen/tobutobugirl-dx/master/LICENSE), [README licence section](https://github.com/SimonLarsen/tobutobugirl-dx#license) |
| tobu-tobu-girl | Tobu Tobu Girl | GB | MIT (code), CC BY 4.0 (all assets) | mirror `roms/tobu-tobu-girl.gb` (from the Homebrew Hub copy, no GitHub release) | [LICENSE](https://raw.githubusercontent.com/SimonLarsen/tobutobugirl/master/LICENSE), [README licence section](https://raw.githubusercontent.com/SimonLarsen/tobutobugirl/master/README.md) |
| libbet | Libbet and the Magic Floor | GB | zlib | mirror `roms/libbet.gb` (Homebrew Hub copy, no GitHub release) | [LICENSE](https://raw.githubusercontent.com/pinobatch/libbet/master/LICENSE), [hh.gbdev.io entry](https://hh.gbdev.io/game/libbet) |
| adjustris | Adjustris | GB | CC0 1.0 | author release [adjustris.gb](https://github.com/tbsp/Adjustris/releases/download/v1.1/adjustris.gb) | [LICENSE.md](https://raw.githubusercontent.com/tbsp/Adjustris/master/LICENSE.md) |
| rhythm-land | Rhythm Land | GB | MIT (repo, both authors in the copyright line); bundles MIT, zlib and one GPL-3.0 routine, see ATTRIBUTION | author release [rhythm-land.gb](https://github.com/sinusoid-studios/rhythm-land/releases/download/v1.0.1/rhythm-land.gb) | [LICENSE](https://raw.githubusercontent.com/sinusoid-studios/rhythm-land/master/LICENSE), [ATTRIBUTION.md](https://raw.githubusercontent.com/sinusoid-studios/rhythm-land/master/ATTRIBUTION.md), [itch: "licensed under the MIT License"](https://martendo.itch.io/rhythm-land) |
| carazu | Carazu | GB | GPL-3.0 | mirror `roms/carazu.gb` (Homebrew Hub copy; GitHub release v1.0 has no asset) | [LICENSE.md](https://raw.githubusercontent.com/mholtkamp/carazu/master/LICENSE.md), [hh.gbdev.io entry](https://hh.gbdev.io/game/carazu) |
| sushi-nights | Sushi Nights | GB | MIT (repo; four collaborators credited in the README, copyright line names Zalo) | mirror `roms/sushi-nights.gb` (Homebrew Hub copy, no GitHub release) | [LICENSE](https://raw.githubusercontent.com/Zal0/SushiNights/master/LICENSE), [readme credits](https://raw.githubusercontent.com/Zal0/SushiNights/master/readme.md), [gbdev database entry](https://raw.githubusercontent.com/gbdev/database/master/entries/sushi-nights/game.json) |
| 2048-gb | 2048gb | GB | zlib | mirror `roms/2048-gb.gb` (Homebrew Hub copy; author's own link is stale) | [LICENSE](https://raw.githubusercontent.com/Sanqui/2048-gb/master/LICENSE), [hh.gbdev.io entry](https://hh.gbdev.io/game/2048gb) |
| ucity | µCity | GBC | GPL-3.0-or-later (code), CC BY-SA 4.0 (graphics and music), BSD-2 (GBT Player) | author release [ucity.gbc](https://github.com/AntonioND/ucity/releases/download/v1.3/ucity.gbc) | [gpl-3.0.txt](https://raw.githubusercontent.com/AntonioND/ucity/master/gpl-3.0.txt), [readme.rst licence section](https://raw.githubusercontent.com/AntonioND/ucity/master/readme.rst) |
| geometrix | Geometrix | GBC | GPL-3.0 | mirror `roms/geometrix.gbc` (committed in the repo tree, no release) | [gpl-3.0.txt](https://raw.githubusercontent.com/AntonioND/geometrix/master/gpl-3.0.txt), [repo README](https://github.com/AntonioND/geometrix) |
| flooder | Flooder | GBC | MIT | mirror `roms/flooder.gbc` (committed as `rom/flooder.gb` in the repo, no release) | [LICENSE](https://raw.githubusercontent.com/Obalfour/Flooder/main/LICENSE), [rom folder](https://github.com/Obalfour/Flooder/tree/main/rom) |
| pong-brew | Pong Brew | GBA | MIT | mirror `roms/pong-brew.gba` (committed in the repo root, no release; byte-identical to the file Tinbox bundles) | [LICENSE](https://raw.githubusercontent.com/ZeroDayArcade/Pong-Homebrew-GBA/main/LICENSE) |
| feline | Feline | GBA | MIT (repo-wide, no asset carve-out, no third-party credits) | author release [feline-88.gba](https://github.com/foopod/gbaGamejam2021/releases/download/day-88/feline-88.gba) | [LICENSE](https://raw.githubusercontent.com/foopod/gbaGamejam2021/main/LICENSE) |
| inheritors-of-the-oubliette | Inheritors of the Oubliette | GBA | GPL-3.0 (repo-wide; itch credits list royalty-free SFX libraries and a font, usual for GPL games) | author release [inheritors-of-the-oubliette.gba](https://github.com/DrLancer-X/inheritors-of-the-oubliette/releases/download/v1.2/inheritors-of-the-oubliette.gba) | [LICENSE](https://raw.githubusercontent.com/DrLancer-X/inheritors-of-the-oubliette/master/LICENSE), [itch page](https://mahoushoujomagicalmoestar.itch.io/inheritors-of-the-oubliette) |

Notes on names: Pong is an Atari trademark; the title is the author's own
repository name and the game is a generic two-paddle game, kept as "Pong Brew".
Adjustris is a falling-block game with original name and art.

## Held back: Tinbox starter games that do not pass the Shelf rule

These two ship inside the sideload build already (decided before the Shelf
existed) but are not listed for download until the questions below are
settled. Lifting either is a one-line change to `titles.json`.

| Title | Finding | What would clear it |
|---|---|---|
| Apotris (akouzoukos) | Licence is AGPL-3.0 ([LICENSE.txt](https://gitea.com/akouzoukos/apotris/raw/branch/main/LICENSE.txt)), which does qualify. But Tetris Holding filed a DMCA notice against it on itch.io ([takedown 1499978](https://itch.io/takedowns/1499978), files still suspended) and an earlier one against the GitHub repo, and the only binaries are semi-stable Azure blob zips on akouzoukos.com (Gitea has no releases). | Owner's call on the trademark risk; a stable release asset. |
| BlindJump (Evan Bowman) | Code MIT, GBA build GPL via libgba, but the README reserves the character designs for non-commercial use and says some music tracks are non-commercial ([README](https://raw.githubusercontent.com/evanbowman/blind-jump-portable/master/README.md)). | Written permission from Evan Bowman (GitHub `evanbowman`, itch `evanbowman.itch.io`). |

## Needs permission (good games, no qualifying licence yet)

| Title | System | Why not yet | Ask |
|---|---|---|---|
| Skyland (Evan Bowman) | GBA | Code MPL-2.0, artwork explicitly reserved, stock music and font licensed to the author only; commercial Steam version | github.com/evanbowman, evanbowman.itch.io |
| Anguna: Warriors of Virtue (Nathan Tolbert) | GBA | No licence for the GBA ROM; third-party art and music with unstated terms | nathan@bitethechili.com |
| Tigermoth (Marq Watkin) | GBA | MIT, but no hosted build anywhere except itch; a release asset or permission to mirror an itch download is needed | github.com/pmprog, pmprog.itch.io |
| Celeste Classic GBA (JeffRuLz) | GBA | No licence on the port; the original PICO-8 cart is "No License"; Celeste is a trademark of Maddy Makes Games | github.com/JeffRuLz, maddymakesgames.com |
| Deadeus (izma) | GB | Name your price on itch, no licence, commercial physical edition via Incube8 | twitter.com/iwazaru91, izma.itch.io |
| Dangan GB (snorpung) | GB | Free on itch, no licence, no source | snorpung.itch.io |
| Super Princess' 2092 Exodus (Zalo, sergeeo) | GB | Source is public but has no licence file | github.com/Zal0, sergeeo.itch.io |
| Mindy's Hike (Damian Yerrick) | GB | itch tagged open source with a source zip but no licence text anywhere | github.com/pinobatch |
| Sheep It Up! (Dr. Ludos) | GB | Free ROM on itch, author clearly means it to be shared, but no licence written | twitter.com/ludoscience, drludos.itch.io |
| GB Corp. (Dr. Ludos) | GB | MIT source, but the only prebuilt ROM is sold for $5; ask before shipping a self-built one | twitter.com/ludoscience |
| Shock Lobster (Dave VanEe) | GB | zlib code and CC BY music, but the enemy graphics are third-party art the author could not open-source | tbsp.itch.io, github.com/tbsp |
| GB-Wordyl (bbbbbr) | GB | GPL-3.0, qualifies, but the current 1.0.8 ROM is only on itch; the only stable mirror is the old 0.85 build | github.com/bbbbbr (ask for a release asset) |

## Checked and excluded

| Title | Reason |
|---|---|
| Varooom 3D, Butano Fighter (Butano demos) | zlib code, but music and art are CC BY-NC-SA (Varooom also embeds eJay voice samples) |
| Symbol Merged | MIT code, all graphics CC BY-NC, splash CC BY-NC-ND |
| GBA Microjam '23 | MIT code, compilation assets declared CC BY-NC 4.0 |
| Goodboy Galaxy demo | Commercial, closed, no licence |
| Petris | Sidebar says MIT, the LICENSE file is CC BY-NC-SA 4.0 |
| Tuff | Code MIT, art "all rights reserved", no ROM |
| Infinity (GBC) | GPL code, assets CC BY-NC-ND and BY-NC-SA, commercial Incube8 release |
| The Machine, Repugnant Bounty, Dragonborne, Micro Mages | Commercial |
| Quartet (GB) | No licence and a port of Photon Storm's game |
| Old Towers | No GB/GBC version exists, and CC BY-NC-SA |
| OpenLara, GBADoom, Quake GBA | Engines need copyrighted game data |
| Evoland.gb, Atari Boxing GBC, pokered-gbc, Doctor How | Third-party IP or ROM hacks |
