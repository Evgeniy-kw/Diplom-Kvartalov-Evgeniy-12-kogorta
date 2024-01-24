# Кварталов Евгений, 12-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request


def test_order_info_by_track():
    track = sender_stand_request.create_order().json()['track']
    response = sender_stand_request.order_info_about_track(track)
    assert response.status_code == 200
