from django.conf.urls import include
from django.urls import re_path
from testapp.views import (AuthorCRUD, InvoiceCRUD, IndexView, CustomerCRUD,
                           LineCRUD, AddressCRUD)

authorcrud = AuthorCRUD()
invoicecrud = InvoiceCRUD()
customercrud = CustomerCRUD()
linecrud = LineCRUD()
addresscrud = AddressCRUD()

urlpatterns = [
    re_path(r'^$', IndexView.as_view()),
    re_path(r'', include(authorcrud.get_urls())),
    re_path(r'', include(invoicecrud.get_urls())),
    re_path(r'', include(customercrud.get_urls())),
    re_path(r'', include(linecrud.get_urls())),
    re_path(r'', include(addresscrud.get_urls())),
    ]
