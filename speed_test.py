import speedtest
import datetime
class SpeedTester():
    def run_test(self):
        st=speedtest.Speedtest()
        st.get_best_server()
        download1=st.download()/ 1_000_000
        upload1=st.upload()/ 1_000_000
        ping1=st.results.ping
        time_2=datetime.datetime.now()
        time_1=str(time_2)
        sonuc={'Download':download1,
            'Upload':upload1,
            'Ping':ping1,
            'Time':time_1}
        return sonuc

 