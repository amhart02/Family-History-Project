from familyhistoryinformation import ah_calculate_age, ah_find_ancestor, ah_search_in_list 
import pytest

def test_calculate_age():
    assert ah_calculate_age(1909, 1920) == 11
    assert ah_calculate_age(1883, 1930) == 47

def test_find_ancestor():
    assert ah_find_ancestor("william", ancestor_list) == ['William', 'Kirk', '1864', '1907', '1893', '1864']
    assert ah_find_ancestor("Peter", ancestor_list) == ['Peter', 'Fire', '1865', '1933', '1885', '1867']

def test_search_in_file(): 
    assert ah_search_in_list("Harry", ancestor_list) == True 
    assert ah_search_in_list("olivia", ancestor_list) == False

ancestor_list = [['Judy', 'Smith', '1909', '1980', '1930', '1909'], 
['John', 'Wilden', '1887', '1970', '1922', ''], 
['Harold', 'Jones', '1920', '1921', '', '1920'], 
['Peter', 'Fire', '1865', '1933', '1885', '1867'], 
['Cindy', 'Dickinson', '1889', '1990', '1930', ''], 
['Richard', 'Oscarson', '1829', '1900', '1859', '1833'], 
['Cynthia', 'Hill', '1777', '1853', '1801', '1777'], 
['Harry', 'Jones', '1866', '1880', '', '1874'], 
['Susan', 'Thornton', '1939', '1949', '', ''], 
['Tricia', 'Cunningham', '1855', '1910', '1880', '1855'], 
['Lucy', 'Christensen', '1899', '1960', '1922', '1899'], 
['Henry', 'Jacobs', '1799', '1801', '', ''], 
['Wendy', 'Larson', '1888', '1945', '1922', '1921'], 
['Robert', 'Paulson', '1923', '1999', '1955', '1923'], 
['Michael', 'Henry', '1785', '1785', '', '1785'], 
['Patricia', 'Johnson', '1903', '1984', '1930', '1911'], 
['William', 'Kirk', '1864', '1907', '1893', '1864'], 
['Paul', 'Freeman', '1944', '1966', '1966', '1944'], 
['Dorothy', 'Dansel', '1808', '1901', '1867', '1808'], 
['Allen', 'Isaac', '1932', '1934', '', '1933'], 
['Jude', 'Belt', '1834', '1888', '1854', '1835'], 
['Phillip', 'Daniels', '1792', '1882', '1820', '1792']]

pytest.main(["-v", "--tb=line", "-rN", __file__])