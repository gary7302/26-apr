from django.urls import path
from .views import *
from store.controller import authview,cartview,checkview,chineseview,paymentview,hindiview,spanishview,frenchview,arabicview,bengaliview,russianview,portugueseview,urduview,indonesianview,germanview,nigerianview,japaneseview,marathiview,teluguview
from django.views.i18n import set_language

urlpatterns = [
    path('',home,name='home'),
    path('type/<str:slug>',type,name='type'),
    path('register',authview.register,name='register'),
    path('chinese-register',chineseview.register,name='chinese-register'),
    path('hindi-register',hindiview.register,name='hindi-register'),
    path('spanish-register',spanishview.register,name='spanish-register'),
    path('french-register',frenchview.register,name='french-register'),
    path('arabic-register',arabicview.register,name='arabic-register'),
    path('bengaliregister',bengaliview.register,name='bengaliregister'),
    path('russianregister',russianview.register,name='russianregister'),
    path('portugueseregister',portugueseview.register,name='portugueseregister'),
    path('urduregister',urduview.register,name='urduregister'),
    path('indonesianregister',indonesianview.register,name='indonesianregister'),
    path('germanregister', germanview.register, name='germanregister'),
    path('japaneseregister', japaneseview.register, name='japaneseregister'),
    path('nigerianregister', nigerianview.register, name='nigerianregister'),
    path('marathiregister', marathiview.register, name='marathiregister'),
    path('teluguregister', teluguview.register, name='teluguregister'),
    path('login',authview.loginpage,name='loginpage'),
    path('hindilogin',authview.hindiloginpage,name='hindilogin'),
    path('chineselogin',authview.chineseloginpage,name='chineselogin'),
    path('spanishlogin',authview.spanishloginpage,name='spanishlogin'),
    path('frenchlogin',authview.frenchloginpage,name='frenchlogin'),
    path('arabiclogin',authview.arabicloginpage,name='arabiclogin'),
    path('bengalilogin',authview.bengaliloginpage,name='bengalilogin'),
    path('russianlogin',authview.russianloginpage,name='russianlogin'),
    path('portugueselogin',authview.portugueseloginpage,name='portugueselogin'),
    path('urdulogin',authview.urduloginpage,name='urdulogin'),
    path('indonesianlogin',authview.indonesianloginpage,name='indonesianlogin'),
    path('germanlogin', authview.germanloginpage, name='germanlogin'),
    path('japaneselogin', authview.japaneseloginpage, name='japaneselogin'),
    path('nigerianlogin', authview.nigerianloginpage, name='nigerianlogin'),
    path('marathilogin', authview.marathiloginpage, name='marathilogin'),
    path('telugulogin', authview.teluguloginpage, name='telugulogin'),
    path('logout',authview.logoutpage,name='logoutpage'),
    path('add-to-cart',cartview.addtocart,name='addtocart'),
    path('cart',cartview.showCart,name='cart'),
    path('chinesecart',cartview.chinesecart,name='chinesecart'),
    path('hindicart',cartview.hindicart,name='hindicart'),
    path('spanishcart',cartview.spanishcart,name='spanishcart'),
    path('frenchcart',cartview.frenchcart,name='frenchcart'),
    path('arabiccart',cartview.arabiccart,name='arabiccart'),
    path('bengalicart',cartview.bengalicart,name='bengalicart'),
    path('russiancart',cartview.russiancart,name='russiancart'),
    path('portuguesecart',cartview.portuguesecart,name='portuguesecart'),
    path('urducart',cartview.urducart,name='urducart'),
    path('indonesiancart',cartview.indonesiancart,name='indonesiancart'),
    path('germancart', cartview.germancart, name='germancart'),
    path('japanesecart', cartview.japanesecart, name='japanesecart'),
    path('nigeriancart', cartview.nigeriancart, name='nigeriancart'),
    path('marathicart', cartview.marathicart, name='marathicart'),
    path('telugucart', cartview.telugucart, name='telugucart'),
    path('update-cart',cartview.updatecart,name="updatecart"),
    path('delete-cart-item',cartview.deletecartitem,name="deletecartitem"),
    path('checkout',checkview.checkout,name='checkout'),
    path('maincheckout',checkview.maincheckout,name='maincheckout'),
    path('chinesemaincheckout',checkview.chinesemaincheckout,name='chinesemaincheckout'),
    path('hindimaincheckout',checkview.hindimaincheckout,name='hindimaincheckout'),
    path('spanishmaincheckout',checkview.spanishmaincheckout,name='spanishmaincheckout'),
    path('frenchmaincheckout',checkview.frenchmaincheckout,name='frenchmaincheckout'),
    path('arabicmaincheckout',checkview.arabicmaincheckout,name='arabicmaincheckout'),
    path('bengalimaincheckout',checkview.bengalimaincheckout,name='bengalimaincheckout'),
    path('russianmaincheckout',checkview.russianmaincheckout,name='russianmaincheckout'),
    path('portuguesemaincheckout',checkview.portuguesemaincheckout,name='portuguesemaincheckout'),
    path('urdumaincheckout',checkview.urdumaincheckout,name='urdumaincheckout'),
    path('indonesianmaincheckout',checkview.indonesianmaincheckout,name='indonasianmaincheckout'),
    path('germanmaincheckout', checkview.germanmaincheckout, name='germanmaincheckout'),
    path('japanesemaincheckout', checkview.japanesemaincheckout, name='japanesemaincheckout'),
    path('nigerianmaincheckout', checkview.nigerianmaincheckout, name='nigerianmaincheckout'),
    path('marathimaincheckout', checkview.marathimaincheckout, name='marathimaincheckout'),
    path('telugumaincheckout', checkview.telugumaincheckout, name='telugumaincheckout'),
    path('place-order',checkview.placeorder,name="placeorder"),
    path('charge', paymentview.charge, name='charge'),
    path('success/', paymentview.success, name='success'),
    path('comment/<int:id>', comment, name='comment'),
    path('chinese-comment/<int:id>',chineseview.comment,name='chinese-comment'),
    path('addComment/<int:id>', addComment, name='addComment'),
    path('chinese-addcomment/<int:id>',chineseview.addComment,name='chinese-addcomment'),
    #path('set-language/', set_language, name='set_language'),
    path('chinese',chineseview.chinesehome,name='chinese'),
    path('hindi',hindiview.hindihome,name='hindi'),
    path('spanish',spanishview.spanishhome,name='spanish'),
    path('french',frenchview.frenchhome,name='french'),
    path('arabic',arabicview.arabichome,name='arabic'),
    path('bengali',bengaliview.bengalihome,name='bengali'),
    path('russian',russianview.russianhome,name='russian'),
    path('portuguese',portugueseview.portuguesehome,name='portuguese'),
    path('urdu',urduview.urduhome,name='urdu'),
    path('indonesian',indonesianview.indonesianhome,name='indonesian'),
    path('german',germanview.germanhome,name='german'),
    path('japanese', japaneseview.japanesehome, name='japanese'),
    path('nigerian', nigerianview.nigerianhome, name='nigerian'),
    path('marathi', marathiview.marathihome, name='marathi'),
    path('telugu', teluguview.teluguhome, name='telugu'),
    path('details',details,name='details'),
    path('chinese-details',chineseview.chinesedetails,name='chinese-details'),
    path('hindi-details',hindiview.hindidetails,name='hindi-details'),
    path('spanish-details',spanishview.spanishdetails,name='spanish-details'),
    path('frenchdetails',frenchview.frenchdetails,name='frenchdetails'),
    path('arabic-details',arabicview.arabicdetails,name='arabic-details'),
    path('bengalidetails',bengaliview.bengalidetails,name='bengalidetails'),
    path('russiandetails',russianview.russiandetails,name='russiandetails'),
    path('portuguesedetails',portugueseview.portuguesedetails,name='portuguesedetails'),
    path('urdudetails',urduview.urdudetails,name='urdudetails'),
    path('indonesiandetails',indonesianview.indonesiandetails,name='indonesiandetails'),
    path('germandetails', germanview.germandetails, name='germandetails'),
    path('japanesedetails', japaneseview.japanesedetails, name='japanesedetails'),
    path('nigeriandetails', nigerianview.nigeriandetails, name='nigeriandetails'),
    path('marathidetails', marathiview.marathidetails, name='marathidetails'),
    path('telugudetails', teluguview.telugudetails, name='telugudetails'),
    path('getpatch',getpatch,name='getpatch'),
    path('chinese-getpatch',chineseview.chinesegetpatch,name='chinese-getpatch'),
    path('hindi-getpatch',hindiview.hindigetpatch,name='hindi-getpatch'),
    path('french-getpatch',frenchview.frenchgetpatch,name='french-getpatch'),
    path('spanish-getpatch',spanishview.spanishgetpatch,name='spanish-getpatch'),
    path('arabic-getpatch',arabicview.arabicgetpatch,name='arabic-getpatch'),
    path('bengaligetpatch',bengaliview.bengaligetpatch,name='bengaligetpatch'),
    path('russiangetpatch',russianview.russiangetpatch,name='russiangetpatch'),
    path('portuguesegetpatch',portugueseview.portuguesegetpatch,name='portuguesegetpatch'),
    path('urdugetpatch',urduview.urdugetpatch,name='urdugetpatch'),
    path('indonesiangetpatch',indonesianview.indonesiangetpatch,name='indonesiangetpatch'),
    path('germangetpatch', germanview.germangetpatch, name='germangetpatch'),
    path('japanesegetpatch', japaneseview.japanesegetpatch, name='japanesegetpatch'),
    path('nigeriangetpatch', nigerianview.nigeriangetpatch, name='nigeriangetpatch'),
    path('marathigetpatch', marathiview.marathigetpatch, name='marathigetpatch'),
    path('telugugetpatch', teluguview.telugugetpatch, name='telugugetpatch'),
    path('usepatch',usepatch,name='usepatch'),
    path('chinese-usepatch',chineseview.chineseusepatch,name='chinese-usepatch'),
    path('hindi-usepatch',hindiview.hindiusepatch,name='hindi-usepatch'),
    path('french-usepatch',frenchview.frenchusepatch,name='french-usepatch'),
    path('spanish-usepatch',spanishview.spanishusepatch,name='spanish-usepatch'),
    path('arabic-usepatch',arabicview.arabicusepatch,name='arabic-usepatch'),
    path('bengaliusepatch',bengaliview.bengaliusepatch,name='bengaliusepatch'),
    path('russianusepatch',russianview.russianusepatch,name='russianusepatch'),
    path('portugueseusepatch',portugueseview.portugueseusepatch,name='portugueseusepatch'),
    path('urduusepatch',urduview.urduusepatch,name='urduusepatch'),
    path('indonesianusepatch',indonesianview.indonesianusepatch,name='indonesianusepatch'),
    path('germanusepatch',germanview.germanusepatch,name='germanusepatch'),
    path('japaneseusepatch', japaneseview.japaneseusepatch, name='japaneseusepatch'),
    path('nigerianusepatch', nigerianview.nigerianusepatch, name='nigerianusepatch'),
    path('marathiusepatch', marathiview.marathiusepatch, name='marathiusepatch'),
    path('teluguusepatch', teluguview.teluguusepatch, name='teluguusepatch'),
    path('hindicomment/<int:id>',hindiview.hindicomment,name='hindicomment'),
    path('hindiaddComment/<int:id>',hindiview.hindiaddcomment,name='hindiaddComment'),
    path('spanishcomment/<int:id>',spanishview.spanishcomment,name='spanishcomment'),
    path('spanishaddcomment/<int:id>',spanishview.spanishaddcomment,name='spanishaddcomment'),
    path('frenchcomment/<int:id>',frenchview.frenchcomment,name='frenchcomment'),
    path('frenchaddcomment/<int:id>',frenchview.frenchaddcomment,name='frenchaddcomment'),
    path('arabiccomment/<int:id>',arabicview.arabiccomment,name='arabiccomment'),
    path('arabicaddcomment/<int:id>',arabicview.arabicaddcomment,name='arabicaddcomment'),
    path('bengalicomment/<int:id>',bengaliview.bengalicomment,name='bengalicomment'),
    path('bengaliaddcomment/<int:id>',bengaliview.bengaliaddcomment,name='bengaliaddcomment'),
    path('russiancomment/<int:id>',russianview.russiancomment,name='russiancomment'),
    path('russianaddcomment/<int:id>',russianview.russianaddcomment,name='russianaddcomment'),
    path('portuguesecomment/<int:id>',portugueseview.portuguesecomment,name='portuguesecomment'),
    path('portugueseaddcomment/<int:id>',portugueseview.portugueseaddcomment,name='portugueseaddcomment'),
    path('urducomment/<int:id>',urduview.urducomment,name='urducomment'),
    path('urduaddcomment/<int:id>',urduview.urduaddcomment,name='urduaddcomment'),
    path('indonesiancomment/<int:id>',indonesianview.indonesiancomment,name='indonesiancomment'),
    path('indonesianaddcomment/<int:id>',indonesianview.indonesianaddcomment,name='indonesianaddcomment'),
    path('germancomment/<int:id>',germanview.germancomment,name='germancomment'),
    path('germanaddcomment/<int:id>',germanview.germanaddcomment,name='germanaddcomment'),
    path('japanesecomment/<int:id>', japaneseview.japanesecomment, name='japanesecomment'),
    path('japaneseaddcomment/<int:id>', japaneseview.japaneseaddcomment, name='japaneseaddcomment'),
    path('nigeriancomment/<int:id>', nigerianview.nigeriancomment, name='nigeriancomment'),
    path('nigerianaddcomment/<int:id>', nigerianview.nigerianaddcomment, name='nigerianaddcomment'),
    path('marathicomment/<int:id>', marathiview.marathicomment, name='marathicomment'),
    path('marathiaddcomment/<int:id>', marathiview.marathiaddcomment, name='marathiaddcomment'),
    path('telugucomment/<int:id>', teluguview.telugucomment, name='telugucomment'),
    path('teluguaddcomment/<int:id>', teluguview.teluguaddcomment, name='teluguaddcomment'),
    path('shopping',shopping,name='shopping'),
]