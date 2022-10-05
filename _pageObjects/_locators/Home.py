from appium.webdriver.common.mobileby import MobileBy


class HomeLocators(object):
    LABEL_USER_NAME = (
        MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/\
                        android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/\
                        android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/\
                        android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView")

    BUTTON_MORE_INFO = (
        MobileBy.XPATH, "//android.widget.SeekBar[@content-desc='Bottom Sheet']/android.view.ViewGroup/android.view.ViewGroup/\
                        android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup")

    BUTTON_MY_POINT = (
        MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/\
                        android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/\
                        android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/\
                        android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.ScrollView/\
                        android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.HorizontalScrollView/\
                        android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/\
                        android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]")
