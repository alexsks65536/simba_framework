from views import Index, Pizza, Foods, Drinks

# Набор привязок: путь-контроллер
routes = {
    '/': Index(),
    '/index/': Index(),
    '/pizza/': Pizza(),
    '/foods/': Foods(),
    '/drinks/': Drinks(),
}
