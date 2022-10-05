from appium.webdriver.common.mobileby import MobileBy


class MyPointLocators(object):
    TEXT_STATUS_OFFICEHOUR = (
        MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/\
                        android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/\
                        android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/\
                        android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/\
                        android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[2])")
