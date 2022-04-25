from typing import List


class InfoMessage:
    """Информационное сообщение о тренировке."""
    pass


class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        LEN_STEP = 0.65
        M_IN_KM = 1000
        dist = self.action * LEN_STEP / M_IN_KM 
        return dist

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = Training.get_distance() / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        # Логика подсчета калорий для каждого вида тренировки будет своя
        # в базовом классе не нужно описывать поведение метода
        # в его теле останется ключевое слово pass
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        # возвращает объект класса сообщения.
        # значит нужен экземпляр класса InfoMessage?
        pass


class Running(Training):
    """Тренировка: бег."""
    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        M_IN_KM = 1000
        spent_calories = (coeff_calorie_1 * Training.get_mean_speed - coeff_calorie_2) * self.weight / M_IN_KM * self.duration 
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self, 
                 action: int, 
                 duration: float, 
                 weight: float,
                 height: float
                 ) -> None:

        super().__init__(action, duration, weight)
        self.height = height
    
    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 0.035
        coeff_calorie_2 = 0.029
        spent_calories = (coeff_calorie_1 * self.weight + (Training.get_mean_speed**2 // self.height) * coeff_calorie_2 * self.weight) * self.duration
        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""
    def __init__(self, 
                 action: int, 
                 duration: float, 
                 weight: float,
                 length_pool: float,
                 count_pool: float
                 ) -> None:

        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        M_IN_KM = 1000
        mean_speed = self.length_pool * self.count_pool / M_IN_KM / self.duration
        return mean_speed
    
    def get_spent_calories(self) -> float:
        coeff_calorie_1 = 1.1
        coeff_calorie_2 = 2
        spent_calories = (Swimming.get_mean_speed() + coeff_calorie_1) * coeff_calorie_2 * self.weight 
        return spent_calories


def read_package(workout_type: str, data: List[float]) -> Training:
    """Прочитать данные полученные от датчиков."""
    action, duration, weight
    return


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]
    
    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

