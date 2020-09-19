using System;
using System.IO;

class MainClass {

  // Лаба 1. Задание 1
  static void l1z1(){
    OperatingSystem os = Environment.OSVersion;
    Console.WriteLine("Платформа: {0}\nВремя: {1}",os.Platform,DateTime.Now);
  }

  // Лаба 1. Задание 2
  static void l1z2(){
    Console.Write("Введите х: ");
    double x = double.Parse(Console.ReadLine());
    double E = 6.3*Math.Sin(1.3*x-Math.PI/3)-x+Math.Sqrt(x+9f/4)+Math.Pow(x+7f/3,2f/3);
    Console.WriteLine("E = {0}",E);
  }

  // Лаба 2. Задание 1
  static void l2z1(){
    Console.Write("Введите А: ");
    float A = Convert.ToSingle(Console.ReadLine());
    Console.Write("Введите I: ");
    int I = Convert.ToInt32(Console.ReadLine());
    Console.Write("Введите C: ");
    double C = Convert.ToDouble(Console.ReadLine());
    Console.Write("Введите L: ");
    bool L = Convert.ToBoolean(Console.ReadLine());
    Console.Write("Введите N: ");
    string N = Console.ReadLine();
    Console.WriteLine("A = {0,15:f3}\n"+
                      "I = {1, 15}\n"+
                      "C = {2, 15:e3}\n"+
                      "L = {3, 15}\n"+
                      "Написал {4,11}",
                      A,I,C,L,N);
  }

  // Лаба 2. Задание 2
  static void l2z2(){
    StreamWriter fileOut = new StreamWriter("out.txt");
    StreamReader fileIn  = new StreamReader("in.txt");
    string s, td = new string('-',28);
    double x, y;
    fileOut.WriteLine("|"+td+"|\n| {0,-26} |\n|"+td+"|\n| {1,-11} | {2,-12} |\n|"+td+"|","Таблица значений","X","Функция");
    reading: s = fileIn.ReadLine();
    if (s == null) goto readed;
    x = Convert.ToDouble(s);
    y = Math.Pow(Math.Sin(x),2)/(x-1);
    fileOut.WriteLine("| X = {0,-7:f4} | Y = {1,-8:f5} |",x,y);
    goto reading;
    readed: fileOut.WriteLine("|"+td+"|\nСоставил Магомедшарипов А.М.");;
    fileOut.Close();
    fileIn.Close();
  }

  // Лаба 3. Задание 1
  static void l3z1(){
    double x = 4, y = 2, z = 3, f, d, F;
    //f = (x*x>y*y?x*x>x*z?x*x:x*z:y*y>x*z?y*y:x*z)+x;
    //d = Math.Pow(x>z?z:x,2)-y;
    if (x*x>y*y) f = x*x;
    else f = y*y;
    if (f < x * z) f = x*z;
    f += x;
    if (x>z) d = z;
    else d = x;
    d = d*d - y;
    if (d == 0){
      Console.Write("Нельзя делить на 0!");
    } else {
      F = f/d;
      Console.Write(F);
    }
  }

  //Лаба 3. Задание 2
  static void l3z2(){
    int N, r = 5;
    m2: Console.Write("Введите х: ");
    float x = float.Parse((Console.ReadLine()));
    Console.Write("Введите y: ");
    float y = float.Parse((Console.ReadLine()));
    if (x*y >= 0){
      if (x*x + y*y <= r*r) {
        if (x > 0) N = 1;
        else N = 2;
      }
      else N = 3;
    }
    else N = 4;
    Console.WriteLine("М("+x+","+y+") лежит в области N = "+N);
    Console.WriteLine("Для повторного ввода нажмите любую клавишу и enter\nДля завершения просто Enter");
    if (Console.ReadLine() != "") goto m2;
  }

  // Лаба 4. Задание 1
  static void l4z1(){
    StreamWriter fileOut = new StreamWriter("l4z1.txt");
    string td = new string('-',28);
    fileOut.WriteLine("|"+td+"|\n| {0,-26} |\n|"+td+"|","Результаты расчёта");
    for (float a = 1; a <= 2; a+=0.25f){
      fileOut.WriteLine("| a = {0,22} |\n|"+td+"|",a);
      for (float x = 0; x <= 10; x+=0.25f){
        double y = a * Math.Pow(x,a)*Math.Pow(Math.E,-x/a);
        fileOut.WriteLine("| X = {0,-7:f2} | Y = {1,-8:f2} |",x,y);
      }
      fileOut.WriteLine("|"+td+"|");
    }
    fileOut.Close();
  }

  // Лаба 4. Задание 2
  static void l4z2(){
    m1: Console.Write("Введите x: ");
    float x = float.Parse(Console.ReadLine());
    double s = 0, y = x/(2-x), a;
    int i = 1;
    a = x/2;
    while (Math.Abs(a)>= 0.000001){
      s += a;
      Console.WriteLine("{2,-4} a = {0,-15:f6} s = {1,-15:f6}",a,s,i+".");
      i++;
      a = Math.Pow(x,i)/Math.Pow(2,i);
    }
    Console.WriteLine("\nФункция x/(2-x) = {0,0:f6}",y);
    Console.WriteLine("Сумма ряда = {0,0:f6}",s);
  }
  // Лаба 5
  static void l5(){
    int N = 10;
    int[] array = new int[N];
    Random rnd = new Random();
    for (int i = 0; i < N; i++){
      array[i] = 7-rnd.Next(10);
      Console.Write(array[i]+(i==N-1?"\n":" "));
    }
    int first = -1,last = 0;
    for (int i = 0; i < N; i++){
      if (array[i]>0){
        if (first == -1) first = i;
        else last = i;
      }
    }
    int tmp = array[first];
    array[first] = array[last];
    array[last] = tmp;
    for (int i = 0; i < N; i++){
      Console.Write(array[i]+(i==N-1?"\n":" "));
    }
  }

  // Лаба 6
  static void l6(){
    int[,] a = new int[4,5];
    int[] D = new int[5];
    int sr = 0, s = 0;
    Random rnd = new Random();
    for (int i = 0; i < 4; i++){
      for (int j = 0; j < 5; j++){
        a[i,j] = 7-rnd.Next(10);
        Console.Write(a[i,j]+(j==4?"\n":" "));
      }
    }
    for (int i = 0; i < 4; i++){
      int sr2 = 0, c = 0;
      for (int j = 0; j < 5; j++){
        if (a[i,j]>0){
          sr2 += a[i,j];
          c++;
        }
      }
      if (sr2/c>sr){
        sr = sr2/c;
        s = i;
      }
    }
    Console.WriteLine("");
    for (int i = 0; i < 5; i++){
      D[i] = a[s,i];
      Console.Write(D[i]+(i==4?"\n":" "));
    }
  }

  // Лаба 7
  class Matrix{
    double[,] a;
    int n;
    public Matrix(int n){
      this.a = new double[n,n];
      this.n = n;
    }
    public void init(int low, int hight){
      Random rnd = new Random();
      for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
          a[i,j] = hight - rnd.Next(hight+1-low);
        }
      }
    }
    public void print(){
      for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
          Console.Write(a[i,j]+(j==n-1?"\n":" "));
        }
      }
    }
    public void setItem(int i, int j, double x){
      a[i,j] = x;
    }
    public double getItem(int i, int j){
      return a[i,j];
    }
    public Matrix mult(Matrix x){
      Matrix m = new Matrix(n);
      double mel;
      for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
          mel = 0;
          for (int k = 0; k < n; k++){
            mel += a[i,k]*x.getItem(k,j);
          }
          m.setItem(i,j,mel);
        }
      }
      return m;
    }
    public bool equals(Matrix x){
      for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
          if (a[i,j] != x.getItem(i,j)) return false;
        }
      }
      return true;
    }
  }
  static void l7(){
    Matrix A = new Matrix(3), B = new Matrix(3);
    A.init(0,9);
    B.init(0,9);
    Console.WriteLine("Матрицы A:");
    A.print();
    Console.WriteLine("\nМатрицы B:");
    B.print();
    if (A.mult(B).equals(B.mult(A))){
      Console.WriteLine("Матрицы перестановочные");
    } else {
      Console.WriteLine("Матрицы не перестановочные");
    }
  }
  public static void Main () {
    //l1z1();
    //l1z2();
    //l2z1();
    //l2z2();
    //l3z1();
    //l3z2();
    //l4z2();
    //l5();
    //l6();
    l7();
  }
}