# libfuse 3 high-level mini reference

Этот локальный reference достаточен для course guided lab. Scope: high-level synchronous API, `FUSE_USE_VERSION 31`.

## Build

В source до `<fuse.h>`:

```c
#define FUSE_USE_VERSION 31
#include <fuse.h>
```

Compile/link:

```bash
gcc -std=c17 -Wall -Wextra -Wpedantic yourfs.c \
  $(pkg-config fuse3 --cflags --libs) -o yourfs
```

Run foreground/debug-friendly:

```bash
mkdir -p mnt
./yourfs -f mnt
```

Unmount в другом terminal:

```bash
fusermount3 -u mnt
```

На systems, где helper name отличается, используй штатный unmount mechanism environment. Не убивай daemon и не оставляй stale mount намеренно.

## Callback signatures used by course

```c
static int fs_getattr(const char *path,
                      struct stat *st,
                      struct fuse_file_info *fi);

static int fs_readdir(const char *path,
                      void *buf,
                      fuse_fill_dir_t filler,
                      off_t offset,
                      struct fuse_file_info *fi,
                      enum fuse_readdir_flags flags);

static int fs_open(const char *path,
                   struct fuse_file_info *fi);

static int fs_read(const char *path,
                   char *buf,
                   size_t size,
                   off_t offset,
                   struct fuse_file_info *fi);
```

Operations table:

```c
static const struct fuse_operations ops = {
    .getattr = fs_getattr,
    .readdir = fs_readdir,
    .open = fs_open,
    .read = fs_read,
};
```

Entry point can use:

```c
return fuse_main(argc, argv, &ops, user_data);
```

`user_data` lifetime must extend through `fuse_main`/loop; callbacks can retrieve it through FUSE context APIs if needed. For the first lab simple static/read-only state is acceptable.

## `readdir` filler

Typical high-level call for a name:

```c
filler(buf, "name", NULL, 0, FUSE_FILL_DIR_DEFAULTS);
```

Always include `.` and `..` for a normal root directory lab.

## Return convention

Metadata/open/readdir callbacks:

```text
0 success
-negative errno failure
```

`read`:

```text
>=0 number of bytes copied (0 = EOF)
-negative errno failure
```

## Read arithmetic checklist

Before converting `off_t`:

```text
offset >= 0
offset representable for your content length domain
```

Then:

```text
if offset >= len: return 0
available = len - offset
take = min(size, available)
memcpy(buf, content + offset, take)
return take
```

## Minimal metadata

Root:

```text
st_mode = S_IFDIR | 0755
st_nlink = 2
```

Read-only virtual file:

```text
st_mode = S_IFREG | 0444
st_nlink = 1
st_size = content_length
```

Exact timestamps/uid/gid are optional for first lab unless your tests depend on them.

## Version note

libfuse 3 evolves. This course deliberately pins the small lab API to version macro 31; optional external docs are appropriate if you intentionally move the lab to a newer API surface.
