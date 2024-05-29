from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status

from webdriver_manager.chrome import ChromeDriverManager

from .serializers import *
from .models import *

import logging
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException, StaleElementReferenceException

# Define logger
logger = logging.getLogger(__name__)

class MoviesView(APIView): 

    def get(self, request, *args, **kwargs):
        logger.debug("Debug message: This is a debug log message")
        try:
            chrome_options = Options() 
            chrome_options.add_experimental_option("detach", True)

            driver = webdriver.Chrome(options=chrome_options)
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            url = "https://www.scrapethissite.com/pages/ajax-javascript/"
            driver.get(url)
            # driver.implicitly_wait(20)
            wait = WebDriverWait(driver, 20)
            id = 2010
            while id<2016:
                btn_2015 = driver.find_element(By.ID, id)
                btn_2015.click()
                wait.until(EC.visibility_of_element_located((By.TAG_NAME, "tr")))
                rows = driver.find_elements(By.TAG_NAME,"tr")
                data=[]
                for tr in rows:
                    col = tr.find_elements(By.TAG_NAME,"td")
                    if col and len(col)>=3:
                        title = col[0].text
                        nominations = col[1].text
                        awards = col[2].text
                        data.append((id ,title, nominations, awards))
                        scraped_data = MoviesData.objects.create(year=id ,title=title, nominations=nominations, awards=awards)
                id = id+1
            print(data)
        except StaleElementReferenceException as e:
            logger.exception("StaleElementReferenceException occurred during scraping: %s", e)
            return Response({'error': 'StaleElementReferenceException occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except TimeoutException as e:
            logger.exception("Timeout occurred during scraping: %s", e)
            return Response({'error': 'Timeout occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except WebDriverException as e:
            logger.exception("WebDriverException occurred during scraping: %s", e)
            return Response({'error': 'WebDriverException occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.exception(f"Error during scraping: {e}")
            return Response({'error': 'Scraping failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # for table_row in data:
        #     titles = table_row.find_elements(By.CLASS_NAME,"film-title")
        #     for title in titles:
        #         print(title.text)
        finally:
            if driver:
                driver.quit() 
        scraped_data_objects = MoviesData.objects.all()
        serializer = MoviesDataSerializer(scraped_data_objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class HockeyTeamsView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            chrome_options = Options() 
            chrome_options.add_experimental_option("detach", True)

        # driver = webdriver.Chrome(options=chrome_options)
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            url = "https://www.scrapethissite.com/pages/forms/"
            driver.get(url)
            driver.implicitly_wait(20)
            wait = WebDriverWait(driver, 20)
            i=1
            while i<3:
                btn_xpath = f'//a[@href="/pages/forms/?page_num={i}"]'
                btn_i = driver.find_element(By.XPATH, btn_xpath)
                btn_i.click()
                wait.until(EC.visibility_of_element_located((By.TAG_NAME, "tr")))
                rows = driver.find_elements(By.TAG_NAME,"tr")
                data=[]
                for tr in rows:
                    col = tr.find_elements(By.TAG_NAME,"td")
                    if col and len(col)>=3:
                        team_name = col[0].text
                        year = col[1].text
                        wins = col[2].text
                        losses = col[3].text
                        win_percent = col[5].text
                        goals_for = col[6].text
                        goals_against = col[7].text
                        plus_minus = col[8].text
                        data.append((team_name, year, wins, losses, win_percent, goals_for, goals_against, plus_minus))
                        HockeyTeamsData.objects.create(team_name= team_name, year = year, wins = wins, losses = losses, win_percent = win_percent, goals_for = goals_for, goals_against = goals_against, plus_minus = plus_minus)
                i = i+1
                # for table_row in data:
                #     titles = table_row.find_elements(By.CLASS_NAME,"film-title")
                #     for title in titles:
                #         print(title.text)
                    
            print(data)  
        except StaleElementReferenceException as e:
            logger.exception("StaleElementReferenceException occurred during scraping: %s", e)
            return Response({'error': 'StaleElementReferenceException occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except TimeoutException as e:
            logger.exception("Timeout occurred during scraping: %s", e)
            return Response({'error': 'Timeout occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except WebDriverException as e:
            logger.exception("WebDriverException occurred during scraping: %s", e)
            return Response({'error': 'WebDriverException occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.exception(f"Error during scraping: {e}")
            return Response({'error': 'Scraping failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # for table_row in data:
        #     titles = table_row.find_elements(By.CLASS_NAME,"film-title")
        #     for title in titles:
        #         print(title.text)
        finally:
            if driver:
                driver.quit() 
        scraped_data_objects = HockeyTeamsData.objects.all()
        serializer = HockeyTeamsDataSerializer(scraped_data_objects, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)