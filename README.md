| URL                         | Desc              | Method                  |
| --------------------------- | ----------------- | ----------------------- |
| /popular_by_place           | 장소 전체 리스트  | GET, POST               |
| /popular_by_place/<int: id> | 장소 상세         | GET, PUT, POST, DELETE  |

- 서버 실행

```bash
$ python manage.py runserver 0.0.0.0:[포트번호]
```
