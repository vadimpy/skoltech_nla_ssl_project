from torchvision.transforms import transforms
from data.gaussian_blur import GaussianBlur


def triple_channel(x):
    return x.repeat(3,1,1)


def get_simclr_data_transforms_train(dataset_name, args):
    s = args["jitter"]

    if dataset_name == 'mnist':
        color_jitter = transforms.ColorJitter(0.8 * s, 0.8 * s, 0.8 * s, 0.2 * s)
        return transforms.Compose([
            transforms.RandomApply([color_jitter], p=0.8),
            transforms.ToTensor(), transforms.Lambda(triple_channel)
        ])

    elif dataset_name == "stl10":
        input_shape = (96,96,3)
        # get a set of data augmentation transformations as described in the SimCLR paper.
        color_jitter = transforms.ColorJitter(0.8 * s, 0.8 * s, 0.8 * s, 0.2 * s)
        return transforms.Compose(
                [
                    transforms.RandomResizedCrop(size=input_shape[0]),
                    transforms.RandomHorizontalFlip(p=args["prob_hflip"]),
                    transforms.RandomApply([color_jitter], p=0.8),
                    transforms.RandomGrayscale(p=args["prob_grayscale"]),
                    GaussianBlur(kernel_size=int(args["blur_sz"] * input_shape[0])),
                    transforms.ToTensor()
                ])

    elif dataset_name in ["cifar10", "cifar100"]:
        # No Gaussian blur since cifar10/100 images is small. 
        return transforms.Compose(
                [
                    transforms.RandomResizedCrop(32),
                    transforms.RandomHorizontalFlip(p=args["prob_hflip"]),
                    transforms.RandomApply([transforms.ColorJitter(0.4 * s, 0.4 * s, 0.4 * s, 0.1 * s)], p=0.8),
                    transforms.RandomGrayscale(p=args["prob_grayscale"]),
                    transforms.ToTensor(),
                    transforms.Normalize([0.4914, 0.4822, 0.4465], [0.2023, 0.1994, 0.2010])
                ])
    else:
        raise RuntimeError(f"unknown dataset: {dataset_name}")


def get_simclr_data_transforms_test(dataset_name):
    if dataset_name in ["cifar10", "cifar100"]:
        return transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize([0.4914, 0.4822, 0.4465], [0.2023, 0.1994, 0.2010])])
    elif dataset_name == "stl10":
        return transforms.Compose([transforms.ToTensor()])

    elif dataset_name == 'mnist':
        return transforms.Compose([transforms.ToTensor(), transforms.Lambda(triple_channel)])

    else:
        raise RuntimeError(f"unknown dataset: {dataset_name}")


def get_simclr_data_transforms(input_shape, s=1):
    color_jitter = transforms.ColorJitter(0.8 * s, 0.8 * s, 0.8 * s, 0.2 * s)
    return transforms.Compose([
        transforms.RandomApply([color_jitter], p=0.8),
        transforms.ToTensor(), transforms.Lambda(triple_channel)
    ])
    