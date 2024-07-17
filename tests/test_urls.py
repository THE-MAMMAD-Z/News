

# class TestUrls(SimpleTestCase) :

#     def test_newslist_url_resolve(self):
#         url = reverse('news:news')
#         self.assertEquals(resolve(url).func , news)

#     def test_search_url_resolve(self):
#         url = reverse('news:search')
#         self.assertEquals(resolve(url).func , search)

#     def test_detail_url_resolve(self):
#         url = reverse('news:detail',args=['1'])
#         self.assertEquals(resolve(url).func , detail_news)

#     def test_home_url_resolve(self):
#         url = reverse('home:home')
#         self.assertEquals(resolve(url).func , home)

#     def test_about_url_resolve(self):
#         url = reverse('home:about')
#         self.assertEquals(resolve(url).func , about)

#     def test_contact_url_resolve(self):
#         url = reverse('home:contact')
#         self.assertEquals(resolve(url).func , contact)


#     def test_category_url_resolve(self):
#         url = reverse('news:category',args=['1'])
#         self.assertEquals(resolve(url).func , categori)