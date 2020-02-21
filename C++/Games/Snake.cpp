// Необходимые библиотеки
#include <iostream>
#include <conio.h>
#include <chrono>
#include <thread>
#include <ctime>
#include <cstdlib>

using namespace std;
// Управление
enum Keys {Left=97,Right=100,Up=119,Down=115,Enter=13,Escape=27,Space=32};
// Начальное направление
int key = Up;
// Размер карты
const unsigned short int MapSize = 30;
// Максимальная длина змеи
const unsigned short int SnakeLen = (MapSize-1)*(MapSize-1);

// Сама змейка
class Snake
{public:
	void init(void);
	void goLeft(void);
	void goRight(void);
	void goUp(void);
	void goDown(void);
	int	 control(void);
private:
	bool run = true;
	int dir;
};
// Инициализация змейки
void Snake::init(void)
{
	dir = key;
}
// Направить змейку влево
void Snake::goLeft(void)
{
	if (dir == Up || dir == Down) dir = Left;
}
// Направить змейку вправо
void Snake::goRight(void)
{
	if (dir == Up || dir == Down) dir = Right;
}
// Направить змейку вверх
void Snake::goUp(void)
{
	if (dir == Left || dir == Right) dir = Up;
}
// Направить змейку вниз
void Snake::goDown(void)
{
	if (dir == Left || dir == Right) dir = Down;
}
// Управление змейкой
int Snake::control(void) {
	if (_kbhit()) {
		key = _getch();
		switch (key)
		{
		case Left:
			goLeft();
			break;
		case Right:
			goRight();
			break;
		case Up:
			goUp();
			break;
		case Down:
			goDown();
			break;
		}
	}
	return dir;
}
// Экран
class Screen
{public:
	void clear(void);
	void update(void);
	void generateMap(void);
	void addObj(void);
	void move(int dir);
	int  getGameState(void);
	int  getSnakeLen(void);
	void gameover(void);
	void gamestart(void);
private:
	int map[MapSize][MapSize];
	int berry[2], coords[SnakeLen][2], snakelen, gameState;
};
// Очистка экрана
void Screen::clear() {
	system("cls");
}
// Перемещение змеи
void Screen::move(int dir) {
	int xx = coords[snakelen - 1][0], yy = coords[snakelen - 1][1];
	for (int i = snakelen-1; i > 0; i--) {
		coords[i][0] = coords[i - 1][0];
		coords[i][1] = coords[i - 1][1];
	}
	if (dir == Up) {
		map[coords[0][0]--][coords[0][1]] = 2;
		map[coords[0][0]][coords[0][1]] = 4;
	}
	else if (dir == Down) {
		map[coords[0][0]++][coords[0][1]] = 2;
		map[coords[0][0]][coords[0][1]] = 4;
	}
	else if (dir == Left) {
		map[coords[0][0]][coords[0][1]--] = 2;
		map[coords[0][0]][coords[0][1]] = 4;
	}
	else if (dir == Right) {
		map[coords[0][0]][coords[0][1]++] = 2;
		map[coords[0][0]][coords[0][1]] = 4;
	}
	if (coords[0][0] == berry[0] && coords[0][1] == berry[1]) {
		addObj();
		coords[snakelen][0] = xx;
		coords[snakelen][1] = yy;
		snakelen++;
	}
	else {
		map[xx][yy] = 0;
	}
	for (int i = 0; i < snakelen; i++) {
		for (int j = 0; j < snakelen; j++) {
			if (coords[i][0] == coords[j][0] && coords[i][1] == coords[j][1] && i != j)
				gameState = 0;
		}
	}
	if (coords[0][0] == 0 || coords[0][0] == MapSize - 1 || coords[0][1] == 0 || coords[0][1] == MapSize - 1)
		gameState = 0;
}
// Состояние игры ( 1 - запущено, 0 - игра окончена)
int Screen::getGameState(void)
{
	return gameState;
}
// Длина змеи
int Screen::getSnakeLen(void)
{
	return snakelen;
}
// Экран при завершении игры
void Screen::gameover(void)
{
	int game_text[5][20] = {
		{0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1},
		{1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0},
		{1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1},
		{1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0},
		{0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1}};
	int over_text[5][20] = {
		{0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0},
		{1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1},
		{1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0},
		{1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0},
		{0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1} };
	for (int i = 0; i < 5; i++)
		for (int j = 0; j < 20; j++) {
			map[9 + i][5 + j] = game_text[i][j];
			map[15 + i][5 + j] = over_text[i][j];
		}
	update();
}
// Начальный экран
void Screen::gamestart(void)
{
	int size_map = (int)sqrt(sizeof(map) / sizeof(int));
	for (int i = 0; i < size_map; i++) {
		for (int j = 0; j < size_map; j++) {
			if (i == 0 or i == size_map - 1 or j == 0 or j == size_map - 1)
				map[i][j] = 1;
			else
				map[i][j] = 0;
		}
	}

	int press_text[5][26] = {
		{0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0},
		{0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0},
		{0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0},
		{0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0},
		{0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0}};

	int enter_text[5][26] = {
		{1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0},
		{1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1},
		{1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0},
		{1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0},
		{1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1}};

	for (int i = 0; i < 5; i++)
		for (int j = 0; j < 26; j++) {
			map[9 + i][2 + j] = press_text[i][j];
			map[15 + i][2 + j] = enter_text[i][j];
		}

	update();
}
// Обновление экрана
void Screen::update() {
	clear();
	for (int i = 0; i < sqrt(sizeof(map) / sizeof(int)); i++) {
		for (int j = 0; j < sqrt(sizeof(map) / sizeof(int)); j++) {
			if (map[i][j] == 1) cout << "# ";
			if (map[i][j] == 0) cout << "  ";
			if (map[i][j] == 2) cout << "o ";
			if (map[i][j] == 4) cout << "O ";
			if (map[i][j] == 3) cout << "* ";
		}
		cout << endl;
	}
}
// Генерация новой карты
void Screen::generateMap(void)
{
	int size_map = (int) sqrt(sizeof(map) / sizeof(int));
	for (int i = 0; i < size_map; i++) {
		for (int j = 0; j < size_map; j++) {
			if (i == 0 or i == size_map -1 or j == 0 or j == size_map-1)
				map[i][j] = 1;
			else
				map[i][j] = 0;
		}
	}
	gameState = 1;
	snakelen = 2;
	coords[0][0] = coords[0][1] = coords[1][0] = size_map / 2;
	coords[1][1] = coords[1][0] - 1;
	map[coords[0][0]][coords[0][0]] = 4;
	map[coords[1][0]][coords[1][1]] = 2;
	addObj();
}
// Добавление объектов на карту
void Screen::addObj(void)
{
	int x, y;
	while (true) {
		x = rand() % ((int) sqrt(sizeof(map) / sizeof(int)));
		y = rand() % ((int)sqrt(sizeof(map) / sizeof(int)));
		if (map[x][y] == 0) {
			map[x][y] = 3;
			berry[0] = x;
			berry[1] = y;
			break;
		}
	}
}

// Сама игра
void GAME() {
	int DIR;
	srand(time(NULL));
	Screen screen;
	Snake snake;
	snake.init();
	screen.gamestart();
	while (key != Enter)
		key = _getch();
	screen.generateMap();
	screen.update();
	while (screen.getGameState()) {
		DIR = snake.control();
		screen.move(DIR);
		this_thread::sleep_for(chrono::milliseconds(100));
		screen.update();
		cout << "Scope: " << screen.getSnakeLen() - 2;
	}
	screen.gameover();
}
int main()
{
	GAME();
}