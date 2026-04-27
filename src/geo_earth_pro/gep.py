"""
Google Earth Pro Image Extractor
Automates image extraction from Google Earth Pro using mouse clicks and keyboard input.
Supports both current imagery and historical imagery downloads with configurable zoom levels.
"""

from . import config
import pyautogui
import pyperclip
import os
import time
import logging
import http.client as httplib
import datetime


class ImageSet:
    """
    Automates downloading satellite imagery from Google Earth Pro.
    
    Supports:
    - Current imagery capture
    - Historical imagery retrieval with multiple time steps
    - Automatic directory organization by date
    - Internet connectivity checks
    """

    def __init__(self, coordinates):
        """
        Initialize ImageSet with target coordinates.
        
        Args:
            coordinates (str): Coordinates in format "latitude, longitude"
        """
        self.coordinates = coordinates
        self.save_mode_active = False
        self.history_mode_active = False
        self.current_mode_active = False
        self.saved_name = False
        
        # Create output folder for current year
        current_year = str(datetime.datetime.now().year)
        self.NEW_FOLDER = os.path.join(config.IMAGES_FOLDER, current_year)
        if not os.path.exists(self.NEW_FOLDER):
            os.makedirs(self.NEW_FOLDER)
        
        # Setup logging
        logging.basicConfig(
            filename='image_extraction.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    @staticmethod
    def check_connection():
        """
        Check internet connectivity to google.com.
        
        Returns:
            bool: True if connected, False otherwise
        """
        conn = httplib.HTTPConnection("www.google.com", timeout=5)
        try:
            conn.request("HEAD", "/")
            conn.close()
            return True
        except:
            conn.close()
            return False

    @staticmethod
    def close_tips():
        """Close Google Earth Pro tip dialogs."""
        pyautogui.click(config.UI_GEP_SCREEN_SIZED['closeTips'])

    @staticmethod
    def modify_saving_options():
        """Configure save panel options for maximum resolution."""
        pyautogui.click(config.UI_GEP_SCREEN_SIZED['savePainel'])
        time.sleep(0.3)
        pyautogui.click(config.UI_GEP_SCREEN_SIZED['savePainelOptions'])
        time.sleep(0.2)
        
        # Select all element options
        for element in ['savePainelOptionsElement1', 'savePainelOptionsElement2',
                        'savePainelOptionsElement3', 'savePainelOptionsElement4']:
            pyautogui.click(config.UI_GEP_SCREEN_SIZED[element])
            time.sleep(0.1)
        
        # Set resolution to maximum
        pyautogui.click(config.UI_GEP_SCREEN_SIZED['savePainelResolutions'])
        time.sleep(0.2)
        pyautogui.click(config.UI_GEP_SCREEN_SIZED['savePainelResolutionMax'])
        time.sleep(0.2)
        pyautogui.click(config.UI_GEP_SCREEN_SIZED['savePainel'])

    def start_searching(self):
        """Search for the target coordinates in Google Earth Pro."""
        # Click search field
        pyautogui.click(config.UI_GEP_SCREEN_SIZED['searchField'])
        time.sleep(0.5)
        
        # Clear existing text
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('delete')
        time.sleep(0.2)
        
        # Type coordinates
        pyautogui.typewrite(self.coordinates)
        time.sleep(0.3)
        
        # Click search button
        pyautogui.click(config.UI_GEP_SCREEN_SIZED['searchButton'])
        time.sleep(2)
        
        self.logger.info(f"Searched for coordinates: {self.coordinates}")

    def zoom_in(self):
        """Zoom to a specific level (approximately 764m)."""
        pyautogui.mouseDown(config.UI_GEP_SCREEN_SIZED['zoomOut'])
        pyautogui.mouseUp(config.UI_GEP_SCREEN_SIZED['zoomOut'])
        time.sleep(0.3)
        
        pyautogui.mouseDown(config.UI_GEP_SCREEN_SIZED['zoomIn'])
        time.sleep(0.6)
        pyautogui.mouseUp(config.UI_GEP_SCREEN_SIZED['zoomIn'])

    def activate_current_imagery(self):
        """Activate current/3D imagery view."""
        if not self.current_mode_active:
            pyautogui.click(config.UI_GEP_SCREEN_SIZED['3dBuildings'])
            self.current_mode_active = True
            time.sleep(0.5)

    def deactivate_current_imagery(self):
        """Deactivate current/3D imagery view."""
        if self.current_mode_active:
            pyautogui.click(config.UI_GEP_SCREEN_SIZED['3dBuildings'])
            self.current_mode_active = False
            time.sleep(0.5)

    def open_history_panel(self):
        """Open historical imagery panel."""
        if not self.history_mode_active:
            pyautogui.click(config.UI_GEP_SCREEN_SIZED['historyButton'])
            self.history_mode_active = True
            time.sleep(0.5)

    def close_history_panel(self):
        """Close historical imagery panel."""
        if self.history_mode_active:
            pyautogui.click(config.UI_GEP_SCREEN_SIZED['historyButton'])
            self.history_mode_active = False
            time.sleep(0.5)

    def get_history_info(self):
        """Extract date from history panel and create appropriate folder."""
        pyautogui.click(config.UI_GEP_SCREEN_SIZED['historyUpdateDate'])
        time.sleep(0.3)
        pyautogui.click(config.UI_GEP_SCREEN_SIZED['historyOpionsDate'])
        time.sleep(0.3)
        pyautogui.click(config.UI_GEP_SCREEN_SIZED['historyGetDate'])
        time.sleep(0.3)
        
        # Copy date text
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        date_str = pyperclip.paste().split()[0]
        
        try:
            date_obj = datetime.datetime.strptime(date_str, '%m/%d/%y')
            date_folder = date_obj.strftime('%Y/%m/%d')
            
            # Create dated folder
            self.NEW_FOLDER = os.path.join(config.IMAGES_FOLDER, date_folder)
            if not os.path.exists(self.NEW_FOLDER):
                os.makedirs(self.NEW_FOLDER)
            
            self.logger.info(f"Created folder: {self.NEW_FOLDER}")
        except ValueError:
            self.logger.warning(f"Could not parse date: {date_str}")
        
        pyautogui.click(config.UI_GEP_SCREEN_SIZED['historyCloseOptionsDate'])
        time.sleep(0.3)

    def move_history_back(self):
        """Move to previous date in history."""
        pyautogui.click(config.UI_GEP_SCREEN_SIZED['moveBackHistory'])
        time.sleep(1)

    def open_save_panel(self):
        """Open the save image panel."""
        if not self.save_mode_active:
            pyautogui.click(config.UI_GEP_SCREEN_SIZED['savePainel'])
            self.save_mode_active = True
            time.sleep(0.5)

    def close_save_panel(self):
        """Close the save image panel."""
        if self.save_mode_active:
            pyautogui.click(config.UI_GEP_SCREEN_SIZED['savePainel'])
            self.save_mode_active = False
            time.sleep(0.5)

    def save_image(self):
        """Save current view as image."""
        self.open_save_panel()
        time.sleep(0.3)
        
        pyautogui.click(config.UI_GEP_SCREEN_SIZED['savePainelSave'])
        time.sleep(0.3)
        
        # Type filename (coordinates) if not already done
        if not self.saved_name:
            pyautogui.typewrite(self.coordinates.replace(', ', '_'))
            self.saved_name = True
            time.sleep(0.3)
        
        # Select output folder
        pyautogui.click(config.UI_GEP_SCREEN_SIZED['selectFolder'])
        time.sleep(0.3)
        pyautogui.typewrite(self.NEW_FOLDER + '\n')
        time.sleep(1)
        
        # Click save
        pyautogui.click(config.UI_GEP_SCREEN_SIZED['saveFile'])
        time.sleep(30)  # Wait for save to complete
        
        self.close_save_panel()
        self.logger.info(f"Saved image for: {self.coordinates}")

    def start_downloading(self):
        """
        Main download workflow:
        1. Search for coordinates
        2. Zoom to target level
        3. Save current imagery
        4. Download historical images from history panel
        """
        # Wait for internet
        while not self.check_connection():
            time.sleep(10)
            self.logger.warning("No internet connection")

        # Search and locate
        self.start_searching()
        time.sleep(2)
        
        pyautogui.click(config.UI_GEP_SCREEN_SIZED['unpinCheck'])
        time.sleep(0.5)
        pyautogui.rightClick(config.UI_GEP_SCREEN_SIZED['pinSelectRightClick'])
        time.sleep(0.3)
        pyautogui.click(config.UI_GEP_SCREEN_SIZED['pinSave'])
        time.sleep(1)

        # Zoom to target level
        self.zoom_in()
        time.sleep(2)

        # Save current imagery
        self.activate_current_imagery()
        time.sleep(1)
        self.save_image()
        time.sleep(2)
        self.deactivate_current_imagery()
        time.sleep(1)

        # Download historical imagery
        self.open_history_panel()
        time.sleep(1)

        self.get_history_info()
        self.save_image()
        time.sleep(2)

        # Move through history and download each date
        for i in range(config.HISTORY_STEPS):
            self.move_history_back()
            time.sleep(2)
            self.get_history_info()
            self.save_image()
            time.sleep(2)

        self.saved_name = False
        self.close_history_panel()
        self.logger.info(f"Completed download for: {self.coordinates}")

    def display_coordinates(self):
        """Display only the coordinates without downloading."""
        while not self.check_connection():
            time.sleep(10)
            self.logger.warning("No internet connection")

        self.start_searching()
        time.sleep(2)
        
        pyautogui.rightClick(config.UI_GEP_SCREEN_SIZED['pinSelectRightClick'])
        time.sleep(0.3)
        pyautogui.click(config.UI_GEP_SCREEN_SIZED['pinSave'])
        
        self.logger.info(f"Displayed coordinates: {self.coordinates}")
