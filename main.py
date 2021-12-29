import speedtest
test = speedtest.Speedtest()
print("Loading server lists....")
test.get_servers()  # ->Get list of servers for speed test
print("Choosing best servers...")
best = test.get_best_server()  # -> choose best servers
# print(best)
print(f"""
      Found    : {best['sponsor']}, 
      Location : {best['name']}
      Country  : {best['country']}
      """)

print("Performing download test....")
download_result = test.download()

print("Performing upload test....")
upload_result = test.upload()

ping_result = test.results.ping


print(f"Download speed  :  {download_result/1024/1024:.2f} Mbbs")
print(f"Upload speed    :  {upload_result/1024/1024:.2f} Mbbs")
print(f"Ping            :  {ping_result:.2f} ms")
