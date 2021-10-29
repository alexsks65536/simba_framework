from views import Index, Style, Pizza, Foods, Drinks, Pizza_logo

# Набор привязок: путь-контроллер
routes = {
    '/': Index(),
    '/index/': Index(),
    '/style/': Style(),
    '/pizza/': Pizza(),
    '/foods/': Foods(),
    '/drinks/': Drinks(),
    '/pizza_logo/': Pizza_logo()
}
