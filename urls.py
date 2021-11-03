from views import Index, Pizza, Foods, Drinks, Contacts

# Набор привязок: путь-контроллер
routes = {
    '/': Index(),
    '/index/': Index(),
    '/pizza/': Pizza(),
    '/foods/': Foods(),
    '/drinks/': Drinks(),
    '/contacts/': Contacts(),
}
