"""
git add .
git commit -m "set"
git push

github.com/tim0212/turn_based_game.git\screen.py
github.com/tim0212/turn_based_game.git\main.py
github.com/tim0212/turn_based_game.git\main_menu.py
github.com/tim0212/turn_based_game.git\text.py
github.com/tim0212/turn_based_game.git\start.py
github.com/tim0212/turn_based_game.git\game.py
github.com/tim0212/turn_based_game.git\charactor.py 

github.com/tim0212/turn_based_game.git

게임 구조
main.py
├─ scene = "start_menu" → start.py의 update()
│   ├─ ↑↓ 선택, 엔터 → scene 전환
│   ├─ "main" → main_scene
│   ├─ "battle" → game
│   └─ "exit" → 종료

├─ scene == "main" → main_scene.update(events)
│   ├─ 플레이어 이동
│   ├─ 적 충돌 시 → "battle"

├─ scene == "battle" → game.update(events)
│   ├─ 플레이어 턴: A키로 공격
│   ├─ 적 자동 반격
│   └─ HP 감소 및 로그 표시

파일구조
object/
├── tiles.py                  ← TileObject 정의
├── charactorname.py          ← 캐릭터 클래스
├── ...
├── enemyname.py              ← 적 클래스
├── ...
├── boss.py                   ← Boss 캐릭터 등
└── __init__.py               ← from . import 캐릭터, 적 등으로 연결

"""