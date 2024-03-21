import g4f
import g4f.api

if __name__ == "__main__":
    print(f'Starting server... [g4f v-{g4f.version.utils.current_version}]')
    g4f.api.Api(engine = g4f, debug = True).run(host="gpt4free.limemarketing.online", port=10000)
